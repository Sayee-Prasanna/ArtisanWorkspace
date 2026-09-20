"""
Pricing Engine
==============
Cost-plus pricing calculator for Indian handicrafts.

Core formula
------------
  base_cost    = material_cost + (labour_hours × hourly_wage)
  retail_price = base_cost × (1 + retail_margin)
  b2b_price    = retail_price × (1 − b2b_discount)

The engine also:
  - Validates the result against known market ranges
  - Generates a human-readable "Why this price" explanation
"""

import math
from market_data import get_craft_data


def calculate_price(
    material_cost: float,
    labour_hours: float,
    hourly_wage: float,
    craft_type: str = "Handicraft",
) -> dict:
    """
    Calculate retail and B2B prices using cost-plus methodology.

    Parameters
    ----------
    material_cost : float
        Total cost of raw materials in INR.
    labour_hours : float
        Number of hours of artisan labour.
    hourly_wage : float
        Artisan's hourly wage in INR.
    craft_type : str
        Craft category (e.g. 'Pottery', 'Weaving'). Used to look up
        market data for margins, discounts, and price validation.

    Returns
    -------
    dict matching the API contract (Section C of COLLABORATION_PLAN.md):
        {
            "retail_price": float,
            "b2b_price": float,
            "market_range": [min, max],
            "explanation": str
        }
    """
    craft_data = get_craft_data(craft_type)
    retail_margin_pct = craft_data["retail_margin_pct"]
    b2b_discount_pct = craft_data["b2b_discount_pct"]
    market_range = craft_data["typical_retail_range"]

    # ── Core cost-plus calculation ───────────────────────────────────
    labour_cost = labour_hours * hourly_wage
    base_cost = material_cost + labour_cost
    retail_price = base_cost * (1 + retail_margin_pct / 100)
    b2b_price = retail_price * (1 - b2b_discount_pct / 100)

    # Round to nearest ₹10 for cleaner pricing
    retail_price = math.ceil(retail_price / 10) * 10
    b2b_price = math.ceil(b2b_price / 10) * 10

    # ── Compute dynamic market range ─────────────────────────────────
    # Blend the static reference range with the computed price
    range_min = min(market_range[0], int(b2b_price * 0.85))
    range_max = max(market_range[1], int(retail_price * 1.15))

    # Ensure the computed price sits within the reported range
    if retail_price < range_min:
        range_min = int(retail_price * 0.85)
    if retail_price > range_max:
        range_max = int(retail_price * 1.15)

    # ── Generate explanation text ────────────────────────────────────
    explanation = _build_explanation(
        material_cost=material_cost,
        labour_hours=labour_hours,
        hourly_wage=hourly_wage,
        base_cost=base_cost,
        retail_price=retail_price,
        b2b_price=b2b_price,
        retail_margin_pct=retail_margin_pct,
        b2b_discount_pct=b2b_discount_pct,
        craft_type=craft_type,
        market_range=(range_min, range_max),
    )

    return {
        "retail_price": float(retail_price),
        "b2b_price": float(b2b_price),
        "market_range": [range_min, range_max],
        "explanation": explanation,
    }


def _build_explanation(
    material_cost: float,
    labour_hours: float,
    hourly_wage: float,
    base_cost: float,
    retail_price: float,
    b2b_price: float,
    retail_margin_pct: float,
    b2b_discount_pct: float,
    craft_type: str,
    market_range: tuple,
) -> str:
    """
    Generate a human-readable "Why this price" explanation.

    The explanation breaks down:
      1. Cost components (materials + labour)
      2. Margin applied and resulting retail price
      3. B2B discount and wholesale price
      4. Comparison to market range
    """
    # Format currency nicely
    def fmt(n):
        return f"\u20b9{n:,.0f}"

    lines = []

    # Cost breakdown
    labour_cost = labour_hours * hourly_wage
    lines.append(
        f"Based on {fmt(material_cost)} in materials and "
        f"{labour_hours:.1f} hours of skilled labour at {fmt(hourly_wage)}/hr "
        f"(labour cost: {fmt(labour_cost)}), "
        f"the base production cost is {fmt(base_cost)}."
    )

    # Margin & retail
    lines.append(
        f"A standard {retail_margin_pct}% {craft_type.lower()} retail margin "
        f"brings the recommended retail price to {fmt(retail_price)}."
    )

    # B2B
    lines.append(
        f"For bulk/B2B orders, a {b2b_discount_pct}% wholesale discount "
        f"gives a B2B price of {fmt(b2b_price)}."
    )

    # Market comparison
    lines.append(
        f"Similar {craft_type.lower()} items typically retail between "
        f"{fmt(market_range[0])} and {fmt(market_range[1])}."
    )

    # Price positioning insight
    mid = (market_range[0] + market_range[1]) / 2
    if retail_price < mid * 0.8:
        lines.append(
            "This price is positioned competitively below the market average, "
            "offering excellent value for buyers."
        )
    elif retail_price > mid * 1.2:
        lines.append(
            "This is a premium-priced piece, justified by higher material "
            "costs and/or labour-intensive craftsmanship."
        )
    else:
        lines.append(
            "This price aligns well with the market average for this craft category."
        )

    return " ".join(lines)


def get_price_breakdown(
    material_cost: float,
    labour_hours: float,
    hourly_wage: float,
    craft_type: str = "Handicraft",
) -> dict:
    """
    Return a detailed cost breakdown (useful for buyer views and reports).

    Returns
    -------
    dict with keys: material_cost, labour_cost, base_cost, retail_margin_pct,
    b2b_discount_pct, retail_price, b2b_price, market_range, craft_type,
    explanation, craft_info
    """
    craft_data = get_craft_data(craft_type)
    pricing = calculate_price(material_cost, labour_hours, hourly_wage, craft_type)

    labour_cost = labour_hours * hourly_wage
    base_cost = material_cost + labour_cost

    return {
        "craft_type": craft_type,
        "material_cost": material_cost,
        "labour_hours": labour_hours,
        "hourly_wage": hourly_wage,
        "labour_cost": labour_cost,
        "base_cost": base_cost,
        "retail_margin_pct": craft_data["retail_margin_pct"],
        "b2b_discount_pct": craft_data["b2b_discount_pct"],
        "retail_price": pricing["retail_price"],
        "b2b_price": pricing["b2b_price"],
        "market_range": pricing["market_range"],
        "explanation": pricing["explanation"],
        "craft_description": craft_data["description"],
    }
