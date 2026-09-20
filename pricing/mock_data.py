"""
Mock Data Layer — Pricing & Market Linkage
==========================================
Hardcoded mock responses matching the API contract defined in
COLLABORATION_PLAN.md Section C: Pricing API (POST /api/pricing/calculate).

Other workstreams can import these to test their integrations
without needing the pricing engine logic.
"""


def mock_pricing_request() -> dict:
    """Return a sample request payload for the pricing API."""
    return {
        "material_cost": 200,
        "labour_hours": 5,
        "hourly_wage": 100,
        "craft_type": "Pottery",
    }


def mock_pricing_response() -> dict:
    """
    Return a mock pricing response matching the API contract.

    Contract (from COLLABORATION_PLAN.md Section C):
    {
        "retail_price": 1250.00,
        "b2b_price": 950.00,
        "market_range": [1000, 1500],
        "explanation": "Based on 5 hours of labour at ₹100/hr, ..."
    }
    """
    return {
        "retail_price": 1250.00,
        "b2b_price": 950.00,
        "market_range": [1000, 1500],
        "explanation": (
            "Based on ₹200 in materials and 5.0 hours of skilled labour "
            "at ₹100/hr (labour cost: ₹500), the base production cost is ₹700. "
            "A standard 35% pottery retail margin brings the recommended "
            "retail price to ₹1,250. "
            "For bulk/B2B orders, a 25% wholesale discount gives a B2B price "
            "of ₹950. "
            "Similar pottery items typically retail between ₹1,000 and ₹1,500. "
            "This price aligns well with the market average for this craft category."
        ),
    }


def mock_pricing_breakdown() -> dict:
    """
    Return a detailed mock breakdown (for buyer view / reports).
    """
    return {
        "craft_type": "Pottery",
        "material_cost": 200.0,
        "labour_hours": 5.0,
        "hourly_wage": 100.0,
        "labour_cost": 500.0,
        "base_cost": 700.0,
        "retail_margin_pct": 35,
        "b2b_discount_pct": 25,
        "retail_price": 1250.00,
        "b2b_price": 950.00,
        "market_range": [1000, 1500],
        "explanation": (
            "Based on ₹200 in materials and 5.0 hours of skilled labour "
            "at ₹100/hr (labour cost: ₹500), the base production cost is ₹700. "
            "A standard 35% pottery retail margin brings the recommended "
            "retail price to ₹1,250. "
            "For bulk/B2B orders, a 25% wholesale discount gives a B2B price "
            "of ₹950. "
            "Similar pottery items typically retail between ₹1,000 and ₹1,500. "
            "This price aligns well with the market average for this craft category."
        ),
        "craft_description": (
            "Traditional Indian pottery ranges from utilitarian terracotta vessels "
            "to ornate painted ceramics. Pricing varies significantly based on "
            "complexity, size, and regional style (Blue Pottery of Jaipur, "
            "Khurja Pottery, Manipuri Black Pottery)."
        ),
    }


def mock_multi_craft_pricing() -> list[dict]:
    """
    Return mock pricing results for multiple craft types.
    Useful for testing catalog exports and buyer views.
    """
    return [
        {
            "craft_type": "Pottery",
            "material_cost": 200,
            "labour_hours": 5,
            "hourly_wage": 80,
            "retail_price": 920.0,
            "b2b_price": 690.0,
            "market_range": [300, 3000],
        },
        {
            "craft_type": "Weaving",
            "material_cost": 800,
            "labour_hours": 20,
            "hourly_wage": 100,
            "retail_price": 3920.0,
            "b2b_price": 3140.0,
            "market_range": [500, 15000],
        },
        {
            "craft_type": "Woodwork",
            "material_cost": 500,
            "labour_hours": 10,
            "hourly_wage": 90,
            "retail_price": 1820.0,
            "b2b_price": 1420.0,
            "market_range": [400, 8000],
        },
        {
            "craft_type": "Metalwork",
            "material_cost": 1200,
            "labour_hours": 8,
            "hourly_wage": 110,
            "retail_price": 2730.0,
            "b2b_price": 2240.0,
            "market_range": [600, 12000],
        },
        {
            "craft_type": "Embroidery",
            "material_cost": 150,
            "labour_hours": 15,
            "hourly_wage": 70,
            "retail_price": 1740.0,
            "b2b_price": 1390.0,
            "market_range": [300, 10000],
        },
    ]
