"""
Pricing Engine — Workstream 4: Pricing & Market Linkage
========================================================
Implements:
1. Cost-plus pricing formulas with retail and B2B wholesale splits.
2. "Why this price?" transparent narrative generation.
3. Market comparable benchmarks across craft categories.
4. Tiered volume pricing calculations for wholesale buyers.
"""

from typing import Dict, Any, List, Optional, Tuple
try:
    from .mock_data import CRAFTS_DATASET, get_craft_by_id
except ImportError:
    from mock_data import CRAFTS_DATASET, get_craft_by_id


# Standard benchmark ranges for handicrafts (in INR)
CRAFT_MARKET_BENCHMARKS: Dict[str, Tuple[int, int]] = {
    "Pottery": (1100, 1650),
    "Terracotta": (1100, 1650),
    "Ceramics": (2400, 3800),
    "Blue Pottery": (2400, 3800),
    "Folk Painting": (3100, 5200),
    "Madhubani": (3100, 5200),
    "Metal Craft": (2100, 3400),
    "Dhokra": (2100, 3400),
    "Handloom Weaving": (4800, 7500),
    "Banarasi": (4800, 7500),
    "Handicraft": (1200, 2500),
}


def calculate_pricing(
    material_cost: float,
    labour_hours: float,
    hourly_wage: float,
    craft_type: str = "Handicraft",
    overhead_cost: float = 0.0,
    retail_margin: float = 0.28,
    b2b_margin: float = 0.14,
    craft_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Calculate retail & B2B price with complete cost-breakdown and
    human-readable 'Why this price?' explanation matching Section C contract.
    """
    material_cost = float(material_cost)
    labour_hours = float(labour_hours)
    hourly_wage = float(hourly_wage)
    overhead_cost = float(overhead_cost)

    # Cost-plus calculations
    labour_cost = round(labour_hours * hourly_wage, 2)
    prime_cost = round(material_cost + labour_cost, 2)
    base_cost = round(prime_cost + overhead_cost, 2)

    # Pricing splits
    retail_price = round(base_cost * (1.0 + retail_margin), 2)
    b2b_price = round(base_cost * (1.0 + b2b_margin), 2)

    # Artisan income share (Artisan earns direct labour wage + 70% of artisan-guild margin)
    artisan_profit_share = round((retail_price - base_cost) * 0.70, 2)
    artisan_total_earnings = round(labour_cost + artisan_profit_share, 2)
    artisan_share_pct = round((artisan_total_earnings / retail_price) * 100, 1) if retail_price > 0 else 0.0

    # Market comparison
    market_range = CRAFT_MARKET_BENCHMARKS.get(craft_type, (int(retail_price * 0.85), int(retail_price * 1.35)))
    if craft_key and craft_key in CRAFTS_DATASET:
        market_range = CRAFTS_DATASET[craft_key]["comparable_market"]["market_range"]

    # Generate "Why this price?" narrative
    explanation = generate_why_this_price(
        craft_type=craft_type,
        material_cost=material_cost,
        labour_hours=labour_hours,
        hourly_wage=hourly_wage,
        retail_margin=retail_margin,
        retail_price=retail_price,
        b2b_price=b2b_price,
        market_range=market_range,
        artisan_total_earnings=artisan_total_earnings,
        artisan_share_pct=artisan_share_pct,
    )

    return {
        "retail_price": retail_price,
        "b2b_price": b2b_price,
        "market_range": list(market_range),
        "explanation": explanation,
        # Extended fields for Buyer View transparency
        "breakdown": {
            "material_cost": material_cost,
            "labour_cost": labour_cost,
            "labour_hours": labour_hours,
            "hourly_wage": hourly_wage,
            "overhead_cost": overhead_cost,
            "base_cost": base_cost,
            "retail_margin_pct": round(retail_margin * 100, 1),
            "b2b_margin_pct": round(b2b_margin * 100, 1),
            "artisan_total_earnings": artisan_total_earnings,
            "artisan_share_pct": artisan_share_pct,
            "middleman_retail_avg": round(sum(market_range) / len(market_range), 2),
            "buyer_savings_pct": round(
                max(0.0, ((sum(market_range) / 2.0) - retail_price) / (sum(market_range) / 2.0) * 100), 1
            )
        }
    }


def generate_why_this_price(
    craft_type: str,
    material_cost: float,
    labour_hours: float,
    hourly_wage: float,
    retail_margin: float,
    retail_price: float,
    b2b_price: float,
    market_range: Tuple[int, int],
    artisan_total_earnings: float,
    artisan_share_pct: float,
) -> str:
    """Generate a clear, trustworthy explanation of the product's price."""
    margin_pct = int(retail_margin * 100)
    return (
        f"Priced fairly at ₹{retail_price:,.2f} based on {labour_hours} hours of skilled craft labour "
        f"at a guaranteed ethical wage of ₹{hourly_wage:,.0f}/hr (₹{labour_hours * hourly_wage:,.0f} labour), "
        f"₹{material_cost:,.0f} in authentic raw materials, and a transparent {margin_pct}% artisan collective margin. "
        f"The artisan receives ₹{artisan_total_earnings:,.2f} ({artisan_share_pct}% of the retail price), "
        f"compared to only ~20% in traditional multi-tier retail channels. "
        f"Similar {craft_type.lower()} items typically retail commercially between ₹{market_range[0]:,} and ₹{market_range[1]:,}."
    )


def calculate_volume_tier(
    craft_data: Dict[str, Any],
    quantity: int
) -> Dict[str, Any]:
    """Calculate the tiered unit price, total price, and savings for a B2B order."""
    pricing = craft_data["pricing_factors"]
    calc = calculate_pricing(
        material_cost=pricing["material_cost"],
        labour_hours=pricing["labour_hours"],
        hourly_wage=pricing["hourly_wage"],
        craft_type=craft_data["craft_type"],
        overhead_cost=pricing.get("overhead_cost", 0.0),
        retail_margin=pricing.get("retail_margin", 0.28),
        b2b_margin=pricing.get("b2b_margin", 0.14),
    )

    retail_unit_price = calc["retail_price"]
    base_b2b_price = calc["b2b_price"]

    # Match tier
    matched_tier = craft_data["b2b_wholesale"]["tiers"][0]
    for tier in craft_data["b2b_wholesale"]["tiers"]:
        if tier["min_qty"] <= quantity <= tier["max_qty"]:
            matched_tier = tier
            break
        elif quantity > tier["max_qty"]:
            matched_tier = tier

    discount_pct = matched_tier["discount_pct"]
    discounted_unit_price = round(retail_unit_price * (1.0 - (discount_pct / 100.0)), 2)
    # Ensure discounted price never falls below base B2B price floor
    unit_price = max(base_b2b_price, discounted_unit_price)

    total_amount = round(unit_price * quantity, 2)
    retail_total = round(retail_unit_price * quantity, 2)
    total_savings = round(retail_total - total_amount, 2)

    return {
        "quantity": quantity,
        "tier_label": matched_tier["label"],
        "discount_pct": discount_pct,
        "retail_unit_price": retail_unit_price,
        "unit_price": unit_price,
        "total_amount": total_amount,
        "retail_total": retail_total,
        "total_savings": total_savings,
        "moq_met": quantity >= craft_data["b2b_wholesale"]["moq"],
        "moq": craft_data["b2b_wholesale"]["moq"],
        "lead_time_days": craft_data["b2b_wholesale"]["lead_time_days"]
    }
