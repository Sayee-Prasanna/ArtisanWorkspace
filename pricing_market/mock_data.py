"""
Mock Data Layer — Workstream 4: Pricing & Market Linkage
=========================================================
Contains realistic datasets for 5 prominent Indian handicraft traditions,
matching the API contracts in COLLABORATION_PLAN.md (Section C & E)
and ONDC Beckn Retail Protocol schema.
"""

from typing import Dict, List, Any

CRAFTS_DATASET: Dict[str, Dict[str, Any]] = {
    "terracotta-pot": {
        "id": "item_tc_001",
        "craft_type": "Pottery",
        "name": "Handcrafted Terracotta Clay Water Pot",
        "hindi_name": "हस्तनिर्मित राजस्थानी मिट्टी का घड़ा (मटका)",
        "tagline": "Natural Evaporative Cooling Pot with Traditional Rajasthani Etchings",
        "category": "Home & Living",
        "subcategory": "Earthenware & Tableware",
        "material": "Natural Alluvial Clay & Terracotta",
        "gi_tagged": False,
        "origin": {
            "village": "Molela",
            "district": "Rajsamand",
            "state": "Rajasthan",
            "region": "Western India"
        },
        "artisan": {
            "name": "Rameshwar Prajapat",
            "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&auto=format&fit=crop&q=80",
            "experience_years": 24,
            "community": "Prajapati Clay Artisans Guild",
            "quote": "Every turn of the potter's wheel carries the wisdom of four generations of clay masters."
        },
        "description": "Hand-thrown on a traditional manual wheel by master artisan Rameshwar Prajapat. Shaped from purified riverbed alluvial clay, naturally sun-baked, and wood-fired in an open earthen pit kiln. Features micro-porous walls for organic evaporative water cooling and hand-etched floral geometric patterns.",
        "dimensions": "Height: 28 cm | Diameter: 24 cm | Capacity: 4.5 Litres",
        "weight": "2.4 kg",
        "care_instructions": "Rinse with plain lukewarm water before first use. Do not use chemical detergents or synthetic soaps.",
        "image_url": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?w=800&auto=format&fit=crop&q=80",
        "pricing_factors": {
            "material_cost": 220.00,
            "material_breakdown": [
                {"item": "Purified Molela Riverbed Clay (10 kg)", "cost": 120.00},
                {"item": "Organic Mustard Oil & Natural Mineral Slips", "cost": 40.00},
                {"item": "Wood & Bio-fuel for Earthen Pit Kiln", "cost": 60.00}
            ],
            "labour_hours": 5.5,
            "hourly_wage": 120.00,
            "overhead_cost": 70.00,
            "retail_margin": 0.28,
            "b2b_margin": 0.14
        },
        "comparable_market": {
            "market_range": [1100, 1650],
            "commercial_retail_avg": 1450,
            "middleman_artisan_share": 25,
            "our_artisan_share": 79
        },
        "b2b_wholesale": {
            "moq": 10,
            "lead_time_days": 12,
            "production_capacity_monthly": 250,
            "tiers": [
                {"min_qty": 1, "max_qty": 9, "discount_pct": 0, "label": "Retail Single"},
                {"min_qty": 10, "max_qty": 49, "discount_pct": 22, "label": "Studio / Boutique"},
                {"min_qty": 50, "max_qty": 99, "discount_pct": 30, "label": "Wholesale Distributor"},
                {"min_qty": 100, "max_qty": 500, "discount_pct": 38, "label": "Bulk Export Partner"}
            ]
        },
        "tags": ["terracotta", "pottery", "clay water pot", "rajasthani", "handmade", "eco-friendly", "cooling matka", "molela"]
    },
    "blue-pottery-vase": {
        "id": "item_bp_002",
        "craft_type": "Ceramics",
        "name": "Jaipur GI Blue Pottery Royal Peacock Vase",
        "hindi_name": "जयपुर जीआई ब्लू पॉटरी मयूर नक्काशी फूलदान",
        "tagline": "Traditional Clay-Free Glazed Ceramic with Persian Cobalt Pigments",
        "category": "Home Decor",
        "subcategory": "Vases & Accent Vessels",
        "material": "Quartz Powder, Glass, Fuller's Earth, Natural Gum & Cobalt Oxide",
        "gi_tagged": True,
        "gi_registration_number": "GI-Appl-No-2",
        "origin": {
            "village": "Kot Jewar",
            "district": "Jaipur",
            "state": "Rajasthan",
            "region": "Northern India"
        },
        "artisan": {
            "name": "Kripal Singh Rathore",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80",
            "experience_years": 31,
            "community": "Jaipur Heritage Blue Pottery Collective",
            "quote": "Blue pottery contains no clay; it is born from pure quartz crystals and fired with cobalt grace."
        },
        "description": "Authentic Geographical Indication (GI) tagged Jaipur Blue Pottery. Crafted using a heritage Indo-Persian dough of powdered quartz, raw glass, katira gond, and multani mitti. Hand-painted with fine squirrel-hair brushes in cobalt blue and turquoise mineral glazes depicting royal peacocks and lotus vines.",
        "dimensions": "Height: 32 cm | Rim Diameter: 12 cm | Base: 14 cm",
        "weight": "1.85 kg",
        "care_instructions": "Wipe with a soft damp microfibre cloth. Fragile; protect against sharp impact. Not suitable for dishwasher.",
        "image_url": "https://images.unsplash.com/photo-1612196808214-b8e1d6145a8c?w=800&auto=format&fit=crop&q=80",
        "pricing_factors": {
            "material_cost": 450.00,
            "material_breakdown": [
                {"item": "High Purity Quartz Stone Powder & Recycled Glass", "cost": 160.00},
                {"item": "Natural Cobalt Oxide & Copper Sulphate Glaze Pigments", "cost": 210.00},
                {"item": "Katira Gond Gum & Multani Mitti Binding Agents", "cost": 80.00}
            ],
            "labour_hours": 9.0,
            "hourly_wage": 150.00,
            "overhead_cost": 120.00,
            "retail_margin": 0.30,
            "b2b_margin": 0.15
        },
        "comparable_market": {
            "market_range": [2400, 3800],
            "commercial_retail_avg": 3200,
            "middleman_artisan_share": 22,
            "our_artisan_share": 81
        },
        "b2b_wholesale": {
            "moq": 6,
            "lead_time_days": 18,
            "production_capacity_monthly": 120,
            "tiers": [
                {"min_qty": 1, "max_qty": 5, "discount_pct": 0, "label": "Retail Single"},
                {"min_qty": 6, "max_qty": 24, "discount_pct": 20, "label": "Gallery & Decor Boutiques"},
                {"min_qty": 25, "max_qty": 49, "discount_pct": 28, "label": "Luxury Interior Retailers"},
                {"min_qty": 50, "max_qty": 200, "discount_pct": 36, "label": "Hotel & Hospitality Bulk"}
            ]
        },
        "tags": ["blue pottery", "jaipur pottery", "gi tagged", "peacock vase", "ceramics", "hand painted", "rajasthan heritage"]
    },
    "madhubani-canvas": {
        "id": "item_mb_003",
        "craft_type": "Folk Painting",
        "name": "Madhubani 'Tree of Life' Natural Dye Wall Art",
        "hindi_name": "मधुबनी हस्तचित्रित 'जीवन वृक्ष' प्राकृतिक कैनवास",
        "tagline": "GI-Certified Mithila Art Painted with Bamboo Twigs and Forest Dyes",
        "category": "Art & Collectibles",
        "subcategory": "Fine Art Paintings",
        "material": "Handmade Tussar Cotton Canvas, Lampblack & Botanical Extracts",
        "gi_tagged": True,
        "gi_registration_number": "GI-Appl-No-45",
        "origin": {
            "village": "Ranti",
            "district": "Madhubani",
            "state": "Bihar",
            "region": "Eastern India"
        },
        "artisan": {
            "name": "Sunita Devi Jha",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&auto=format&fit=crop&q=80",
            "experience_years": 28,
            "community": "Mithila Mahila Kalakar Society",
            "quote": "Our brushes are sharpened bamboo twigs; our ink comes from the roots of turmeric and deep lamp soot."
        },
        "description": "Authentic Kachni and Bharni style Madhubani painting created on cow-dung treated handmade cotton rag paper. Intricately rendered using sharpened bamboo nibs without preliminary pencil sketches. Pigments are 100% natural, extracted from indigo, turmeric root, parijat flowers, kusum leaves, and pure lampblack soot.",
        "dimensions": "45 cm x 60 cm (18 x 24 inches, unframed with 2-inch border)",
        "weight": "0.35 kg",
        "care_instructions": "Frame under UV-protective museum glass. Keep away from direct high humidity and damp surfaces.",
        "image_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pricing_factors": {
            "material_cost": 310.00,
            "material_breakdown": [
                {"item": "Handmade Organic Cotton-Rag Canvas (Cold Pressed)", "cost": 140.00},
                {"item": "Botanical Dyes (Indigo, Turmeric, Kusum, Madder)", "cost": 110.00},
                {"item": "Hand-hewn Bamboo Nibs & Organic Gum Binders", "cost": 60.00}
            ],
            "labour_hours": 14.0,
            "hourly_wage": 140.00,
            "overhead_cost": 90.00,
            "retail_margin": 0.28,
            "b2b_margin": 0.14
        },
        "comparable_market": {
            "market_range": [3100, 5200],
            "commercial_retail_avg": 4200,
            "middleman_artisan_share": 18,
            "our_artisan_share": 84
        },
        "b2b_wholesale": {
            "moq": 5,
            "lead_time_days": 21,
            "production_capacity_monthly": 45,
            "tiers": [
                {"min_qty": 1, "max_qty": 4, "discount_pct": 0, "label": "Retail Collector"},
                {"min_qty": 5, "max_qty": 19, "discount_pct": 18, "label": "Curated Art Galleries"},
                {"min_qty": 20, "max_qty": 49, "discount_pct": 25, "label": "Corporate Gifting Partners"},
                {"min_qty": 50, "max_qty": 100, "discount_pct": 32, "label": "Museum & International Orders"}
            ]
        },
        "tags": ["madhubani", "mithila art", "tree of life", "gi tagged", "natural dyes", "folk painting", "bihar craft", "handmade"]
    },
    "dhokra-nandi": {
        "id": "item_dk_004",
        "craft_type": "Metal Craft",
        "name": "Bastar Dhokra Lost-Wax Bell Metal Nandi",
        "hindi_name": "बस्तर ढोकरा ढलवा पीतल नंदी प्रतिमा",
        "tagline": "4000-Year-Old Lost-Wax Bell Metal Cast from the Deep Forests of Bastar",
        "category": "Home Decor",
        "subcategory": "Sculptures & Heritage Metalware",
        "material": "Recycled Brass, Bronze, Beeswax, Damar Resin & Red Clay",
        "gi_tagged": True,
        "gi_registration_number": "GI-Appl-No-83",
        "origin": {
            "village": "Kondagaon",
            "district": "Bastar",
            "state": "Chhattisgarh",
            "region": "Central India"
        },
        "artisan": {
            "name": "Sukhlal Ghadwa",
            "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80",
            "experience_years": 27,
            "community": "Bastar Ghadwa Bell Metal Guild",
            "quote": "Each wax strand is coiled by thumb; when the furnace glows, the wax departs and metal takes its soul."
        },
        "description": "Handmade using the ancient non-ferrous lost-wax casting technique (cire perdue) dating back to the Indus Valley Dancing Girl. Constructed from fine threads of pure forest beeswax coiled over a clay core, encased in termite-mound clay slip, and filled with molten scrap brass and bronze.",
        "dimensions": "Length: 19 cm | Width: 9 cm | Height: 16 cm",
        "weight": "1.45 kg",
        "care_instructions": "Dust with dry cotton cloth. To restore antique warm glow, gently polish with brass polish or tamarind paste.",
        "image_url": "https://images.unsplash.com/photo-1590736969955-71cc94801759?w=800&auto=format&fit=crop&q=80",
        "pricing_factors": {
            "material_cost": 380.00,
            "material_breakdown": [
                {"item": "Brass & Bronze Bell Metal Ingot Alloy (1.8 kg)", "cost": 220.00},
                {"item": "Wild Beeswax & Sal Resin (Damar)", "cost": 90.00},
                {"item": "Bastar Anthill Termite Clay & Rice Husk Core", "cost": 70.00}
            ],
            "labour_hours": 8.5,
            "hourly_wage": 130.00,
            "overhead_cost": 100.00,
            "retail_margin": 0.30,
            "b2b_margin": 0.15
        },
        "comparable_market": {
            "market_range": [2100, 3400],
            "commercial_retail_avg": 2800,
            "middleman_artisan_share": 24,
            "our_artisan_share": 80
        },
        "b2b_wholesale": {
            "moq": 8,
            "lead_time_days": 15,
            "production_capacity_monthly": 80,
            "tiers": [
                {"min_qty": 1, "max_qty": 7, "discount_pct": 0, "label": "Retail Single"},
                {"min_qty": 8, "max_qty": 29, "discount_pct": 20, "label": "Handicraft Boutiques"},
                {"min_qty": 30, "max_qty": 74, "discount_pct": 28, "label": "Heritage Architecture Decor"},
                {"min_qty": 75, "max_qty": 200, "discount_pct": 35, "label": "Wholesale Export Supply"}
            ]
        },
        "tags": ["dhokra", "bastar art", "bell metal", "lost wax casting", "nandi statue", "brass sculpture", "chhattisgarh", "gi tagged"]
    },
    "banarasi-silk-stole": {
        "id": "item_bs_005",
        "craft_type": "Handloom Weaving",
        "name": "Banarasi Pure Katan Silk Handloom Stole",
        "hindi_name": "बनारसी शुद्ध कतान सिल्क हथकरघा स्टोल (दुपट्टा)",
        "tagline": "Handwoven with Fine Pure Silk Warp and Intricate Zari Butidar Weft",
        "category": "Apparel & Accessories",
        "subcategory": "Scarves, Shawls & Stoles",
        "material": "100% Pure Mulberry Silk & Electroplated Gold Zari",
        "gi_tagged": True,
        "gi_registration_number": "GI-Appl-No-99",
        "origin": {
            "village": "Kotwa",
            "district": "Varanasi",
            "state": "Uttar Pradesh",
            "region": "Northern India"
        },
        "artisan": {
            "name": "Mohammad Rizwan Ansari",
            "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&auto=format&fit=crop&q=80",
            "experience_years": 35,
            "community": "Varanasi Bunkar Handloom Weavers Society",
            "quote": "The rhythmic clatter of our pit loom weaves centuries of Banaras into every inch of silk."
        },
        "description": "Authentic Handloom Mark and Silk Mark certified Banarasi stole. Handwoven on traditional wooden pit looms across 16 days. Embellished with classic shikargah and floral kadhwa zari motifs using pure silk yarns and tested metallic gold threads.",
        "dimensions": "Length: 200 cm | Width: 70 cm (78 x 28 inches)",
        "weight": "0.22 kg",
        "care_instructions": "Dry clean only. Store wrapped in breathable muslin fabric. Do not iron directly on metallic zari.",
        "image_url": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&auto=format&fit=crop&q=80",
        "pricing_factors": {
            "material_cost": 980.00,
            "material_breakdown": [
                {"item": "Pure Mulberry Katan Silk Yarn (350g)", "cost": 650.00},
                {"item": "Metallic Electroplated Gold Zari Thread", "cost": 220.00},
                {"item": "Natural Dyeing & Finishing Sizing", "cost": 110.00}
            ],
            "labour_hours": 16.0,
            "hourly_wage": 160.00,
            "overhead_cost": 140.00,
            "retail_margin": 0.28,
            "b2b_margin": 0.14
        },
        "comparable_market": {
            "market_range": [4800, 7500],
            "commercial_retail_avg": 5900,
            "middleman_artisan_share": 20,
            "our_artisan_share": 82
        },
        "b2b_wholesale": {
            "moq": 6,
            "lead_time_days": 25,
            "production_capacity_monthly": 60,
            "tiers": [
                {"min_qty": 1, "max_qty": 5, "discount_pct": 0, "label": "Retail Single"},
                {"min_qty": 6, "max_qty": 19, "discount_pct": 18, "label": "Designer Ethnic Boutiques"},
                {"min_qty": 20, "max_qty": 49, "discount_pct": 26, "label": "National Departmental Stores"},
                {"min_qty": 50, "max_qty": 150, "discount_pct": 34, "label": "Global Fashion Wholesalers"}
            ]
        },
        "tags": ["banarasi silk", "katan silk", "handloom", "zari work", "varanasi weaver", "silk mark", "gi tagged", "luxury stole"]
    }
}


def get_all_crafts() -> List[Dict[str, Any]]:
    """Return all craft products in the dataset."""
    return list(CRAFTS_DATASET.values())


def get_craft_by_id(craft_key_or_id: str) -> Dict[str, Any]:
    """Retrieve craft product by key or item ID."""
    if craft_key_or_id in CRAFTS_DATASET:
        return CRAFTS_DATASET[craft_key_or_id]
    for key, data in CRAFTS_DATASET.items():
        if data.get("id") == craft_key_or_id:
            return data
    # Fallback to first craft
    return list(CRAFTS_DATASET.values())[0]
