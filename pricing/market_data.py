"""
Market Data — Comparable Price Dataset
=======================================
Reference pricing data for 5 Indian craft categories.

Each craft entry contains:
  - typical_retail_range : (min, max) in INR
  - b2b_discount_pct    : percentage discount for B2B / wholesale
  - retail_margin_pct    : standard retail margin percentage
  - hourly_wage_default  : typical artisan hourly wage in INR
  - description          : brief context for explanation text

This data is used by the pricing engine to:
  1. Validate computed prices against market norms
  2. Provide the market_range field in the API response
  3. Generate the "Why this price" explanation
"""

CRAFT_DATABASE = {
    "Pottery": {
        "typical_retail_range": (300, 3000),
        "b2b_discount_pct": 25,
        "retail_margin_pct": 35,
        "hourly_wage_default": 80,
        "materials": ["Terracotta", "Stoneware", "Ceramic", "Clay"],
        "description": (
            "Traditional Indian pottery ranges from utilitarian terracotta vessels "
            "to ornate painted ceramics. Pricing varies significantly based on "
            "complexity, size, and regional style (Blue Pottery of Jaipur, "
            "Khurja Pottery, Manipuri Black Pottery)."
        ),
    },
    "Weaving": {
        "typical_retail_range": (500, 15000),
        "b2b_discount_pct": 20,
        "retail_margin_pct": 40,
        "hourly_wage_default": 100,
        "materials": ["Cotton", "Silk", "Wool", "Jute", "Bamboo"],
        "description": (
            "Handloom weaving encompasses sarees, shawls, rugs, and fabric. "
            "Products like Banarasi silk, Chanderi, Pochampally Ikat, and "
            "Pashmina command premium prices due to intricate patterns and "
            "high-quality yarns."
        ),
    },
    "Woodwork": {
        "typical_retail_range": (400, 8000),
        "b2b_discount_pct": 22,
        "retail_margin_pct": 30,
        "hourly_wage_default": 90,
        "materials": ["Sandalwood", "Teak", "Sheesham", "Walnut", "Bamboo"],
        "description": (
            "Indian woodcraft includes carved furniture, decorative panels, "
            "toys (Channapatna), and inlay work (Saharanpur). Price depends "
            "on wood type, carving intricacy, and finishing quality."
        ),
    },
    "Metalwork": {
        "typical_retail_range": (600, 12000),
        "b2b_discount_pct": 18,
        "retail_margin_pct": 30,
        "hourly_wage_default": 110,
        "materials": ["Brass", "Copper", "Bronze", "Bell Metal", "Iron"],
        "description": (
            "Metalcraft spans Dhokra casting, Bidriware inlay, brass utensils, "
            "and copper decorative items. Material cost is a significant factor, "
            "with brass and copper commanding higher base prices."
        ),
    },
    "Embroidery": {
        "typical_retail_range": (300, 10000),
        "b2b_discount_pct": 20,
        "retail_margin_pct": 45,
        "hourly_wage_default": 70,
        "materials": ["Cotton", "Silk", "Wool", "Linen", "Thread"],
        "description": (
            "Hand embroidery styles include Chikankari (Lucknow), Phulkari "
            "(Punjab), Kantha (Bengal), Kashida (Kashmir), and Zardozi. "
            "Labour-intensive pieces with fine threadwork command the highest "
            "premiums."
        ),
    },
}


def get_craft_data(craft_type: str) -> dict:
    """
    Look up market data for a given craft type.

    Parameters
    ----------
    craft_type : str
        The craft category (e.g. 'Pottery', 'Weaving').
        Case-insensitive; falls back to a generic 'Handicraft' profile
        if the craft type is not found.

    Returns
    -------
    dict with keys: typical_retail_range, b2b_discount_pct,
    retail_margin_pct, hourly_wage_default, materials, description
    """
    # Try exact match first, then case-insensitive
    craft = CRAFT_DATABASE.get(craft_type)
    if craft is None:
        for key, value in CRAFT_DATABASE.items():
            if key.lower() == craft_type.lower():
                craft = value
                break

    if craft is None:
        # Generic fallback for unrecognized crafts
        craft = {
            "typical_retail_range": (300, 5000),
            "b2b_discount_pct": 20,
            "retail_margin_pct": 30,
            "hourly_wage_default": 85,
            "materials": ["Mixed"],
            "description": (
                "Indian handicraft with pricing based on standard cost-plus "
                "methodology. Market range is estimated from comparable "
                "handmade products."
            ),
        }

    return craft


def get_all_crafts() -> dict:
    """Return the full craft database."""
    return CRAFT_DATABASE.copy()


def get_supported_craft_types() -> list[str]:
    """Return a sorted list of supported craft type names."""
    return sorted(CRAFT_DATABASE.keys())
