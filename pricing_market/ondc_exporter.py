"""
ONDC Schema Exporter — Workstream 4: Pricing & Market Linkage
=============================================================
Transforms artisan craft listings & cost-plus pricing into standard
ONDC (Open Network for Digital Commerce) Beckn Protocol Retail v1.2.0 items,
and exports catalog to JSON & CSV formats.
"""

import csv
import io
import json
from typing import Dict, Any, List, Optional
try:
    from .mock_data import CRAFTS_DATASET, get_all_crafts
    from .pricing_engine import calculate_pricing
except ImportError:
    from mock_data import CRAFTS_DATASET, get_all_crafts
    from pricing_engine import calculate_pricing


def craft_to_ondc_item(craft_data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a craft record into an ONDC Beckn Protocol retail item schema."""
    pf = craft_data["pricing_factors"]
    pricing = calculate_pricing(
        material_cost=pf["material_cost"],
        labour_hours=pf["labour_hours"],
        hourly_wage=pf["hourly_wage"],
        craft_type=craft_data["craft_type"],
        overhead_cost=pf.get("overhead_cost", 0.0),
        retail_margin=pf.get("retail_margin", 0.28),
        b2b_margin=pf.get("b2b_margin", 0.14),
    )

    item_id = craft_data["id"]
    retail_price = f"{pricing['retail_price']:.2f}"
    max_price = f"{pricing['breakdown']['middleman_retail_avg']:.2f}"

    return {
        "id": item_id,
        "descriptor": {
            "name": craft_data["name"],
            "code": f"SKU-{craft_data['id'].upper()}",
            "symbol": craft_data.get("image_url", ""),
            "short_desc": craft_data.get("tagline", craft_data["name"]),
            "long_desc": craft_data.get("description", ""),
            "images": [craft_data.get("image_url", "")],
        },
        "price": {
            "currency": "INR",
            "value": retail_price,
            "maximum_value": max_price,
        },
        "category_id": craft_data.get("category", "Home & Living"),
        "fulfillment_id": "F1_HANDICRAFT_SECURE_EXPRESS",
        "location_id": f"LOC_{craft_data['origin']['state'].upper()[:4]}",
        "matched": True,
        "recommended": True,
        "@ondc/org/returnable": False,
        "@ondc/org/cancellable": True,
        "@ondc/org/available_on_cod": False,
        "@ondc/org/time_to_ship": f"P{craft_data['b2b_wholesale']['lead_time_days']}D",
        "tags": [
            {
                "code": "craft_authenticity",
                "list": [
                    {"code": "craft_type", "value": craft_data["craft_type"]},
                    {"code": "gi_tagged", "value": "true" if craft_data.get("gi_tagged") else "false"},
                    {"code": "gi_registration", "value": craft_data.get("gi_registration_number", "N/A")},
                    {"code": "origin_state", "value": craft_data["origin"]["state"]},
                    {"code": "origin_village", "value": craft_data["origin"]["village"]},
                    {"code": "artisan_name", "value": craft_data["artisan"]["name"]},
                    {"code": "artisan_share_pct", "value": f"{pricing['breakdown']['artisan_share_pct']}%"}
                ]
            },
            {
                "code": "b2b_wholesale_spec",
                "list": [
                    {"code": "b2b_unit_price", "value": f"{pricing['b2b_price']:.2f}"},
                    {"code": "moq", "value": str(craft_data["b2b_wholesale"]["moq"])},
                    {"code": "production_capacity_monthly", "value": str(craft_data["b2b_wholesale"]["production_capacity_monthly"])},
                    {"code": "lead_time_days", "value": str(craft_data["b2b_wholesale"]["lead_time_days"])}
                ]
            },
            {
                "code": "price_transparency",
                "list": [
                    {"code": "labour_hours", "value": str(pf["labour_hours"])},
                    {"code": "hourly_wage", "value": f"INR {pf['hourly_wage']:.0f}"},
                    {"code": "material_cost", "value": f"INR {pf['material_cost']:.2f}"},
                    {"code": "why_this_price", "value": pricing["explanation"]}
                ]
            }
        ]
    }


def generate_ondc_catalog() -> Dict[str, Any]:
    """Generate complete Beckn BPP catalog structure with all crafts."""
    crafts = get_all_crafts()
    items = [craft_to_ondc_item(c) for c in crafts]

    return {
        "context": {
            "domain": "nic2004:52110",
            "country": "IND",
            "city": "std:080",
            "action": "on_search",
            "core_version": "1.2.0",
            "bap_id": "buyer-app.ondc.org",
            "bpp_id": "artisan-network.gov.in",
            "bpp_uri": "https://artisan-network.gov.in/bpp",
            "timestamp": "2026-09-20T18:00:00.000Z"
        },
        "message": {
            "catalog": {
                "bpp/descriptor": {
                    "name": "Bharat Artisan Direct Marketplace (SIH Workstream 4)",
                    "symbol": "https://artisan-network.gov.in/logo.png",
                    "short_desc": "Empowering Rural Artisans via Fair-Wage Cost-Plus Pricing",
                    "long_desc": "Open Network for Digital Commerce verified artisan craft catalog with GI tags and transparent fair-wage cost breakdown."
                },
                "bpp/providers": [
                    {
                        "id": "PROVIDER_BHARAT_ARTISAN_FEDERATION",
                        "descriptor": {
                            "name": "All India Artisans & Craftworkers Guild",
                            "short_desc": "Verified cooperative representing authentic Indian handicraft masters."
                        },
                        "items": items
                    }
                ]
            }
        }
    }


def export_catalog_to_csv(output_file_path: Optional[str] = None) -> str:
    """Export catalog items into a flat CSV format for spreadsheet & ERP ingestion."""
    crafts = get_all_crafts()
    output = io.StringIO()
    writer = csv.writer(output)

    # Header
    writer.writerow([
        "Item_ID",
        "Product_Name",
        "Craft_Type",
        "State",
        "Village",
        "Artisan_Name",
        "GI_Tagged",
        "Retail_Price_INR",
        "B2B_Wholesale_Price_INR",
        "Comparable_Market_Avg_INR",
        "Artisan_Share_Pct",
        "Material_Cost_INR",
        "Labour_Hours",
        "Hourly_Wage_INR",
        "B2B_MOQ",
        "Lead_Time_Days",
        "Tags"
    ])

    for c in crafts:
        pf = c["pricing_factors"]
        p = calculate_pricing(
            material_cost=pf["material_cost"],
            labour_hours=pf["labour_hours"],
            hourly_wage=pf["hourly_wage"],
            craft_type=c["craft_type"],
            overhead_cost=pf.get("overhead_cost", 0.0),
            retail_margin=pf.get("retail_margin", 0.28),
            b2b_margin=pf.get("b2b_margin", 0.14),
        )

        writer.writerow([
            c["id"],
            c["name"],
            c["craft_type"],
            c["origin"]["state"],
            c["origin"]["village"],
            c["artisan"]["name"],
            "Yes" if c.get("gi_tagged") else "No",
            f"{p['retail_price']:.2f}",
            f"{p['b2b_price']:.2f}",
            f"{p['breakdown']['middleman_retail_avg']:.2f}",
            f"{p['breakdown']['artisan_share_pct']}%",
            f"{pf['material_cost']:.2f}",
            pf["labour_hours"],
            f"{pf['hourly_wage']:.0f}",
            c["b2b_wholesale"]["moq"],
            c["b2b_wholesale"]["lead_time_days"],
            "; ".join(c.get("tags", []))
        ])

    csv_content = output.getvalue()
    if output_file_path:
        with open(output_file_path, "w", encoding="utf-8", newline="") as f:
            f.write(csv_content)

    return csv_content
