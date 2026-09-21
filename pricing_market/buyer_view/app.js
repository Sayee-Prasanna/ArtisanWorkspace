/**
 * BharatArtisan Direct — Mock Buyer View Engine
 * Workstream 4: Pricing & Market Linkage Validation
 */

// ── 1. EMBEDDED REALISTIC MULTI-CRAFT DATASET ────────────────────────
const CRAFTS_DATA = {
  "terracotta-pot": {
    id: "item_tc_001",
    craft_type: "Pottery",
    name: "Handcrafted Terracotta Clay Water Pot",
    hindi_name: "हस्तनिर्मित राजस्थानी मिट्टी का घड़ा (मटका)",
    tagline: "Natural Evaporative Cooling Pot with Traditional Rajasthani Etchings",
    category: "Home & Living",
    subcategory: "Earthenware & Tableware",
    material: "Natural Alluvial Clay & Terracotta",
    gi_tagged: false,
    origin: {
      village: "Molela",
      district: "Rajsamand",
      state: "Rajasthan",
      region: "Western India"
    },
    artisan: {
      name: "Rameshwar Prajapat",
      avatar: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&auto=format&fit=crop&q=80",
      experience_years: 24,
      community: "Prajapati Clay Artisans Guild",
      quote: "Every turn of the potter's wheel carries the wisdom of four generations of clay masters."
    },
    description: "Hand-thrown on a traditional manual wheel by master artisan Rameshwar Prajapat. Shaped from purified riverbed alluvial clay, naturally sun-baked, and wood-fired in an open earthen pit kiln. Features micro-porous walls for organic evaporative water cooling and hand-etched floral geometric patterns.",
    dimensions: "Height: 28 cm | Diameter: 24 cm | Capacity: 4.5 Litres",
    weight: "2.4 kg",
    care_instructions: "Rinse with plain lukewarm water before first use. Do not use chemical detergents or synthetic soaps.",
    image_url: "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?w=800&auto=format&fit=crop&q=80",
    pricing_factors: {
      material_cost: 220.00,
      material_breakdown: [
        { item: "Purified Molela Riverbed Clay (10 kg)", cost: 120.00 },
        { item: "Organic Mustard Oil & Mineral Slips", cost: 40.00 },
        { item: "Wood & Bio-fuel for Earthen Pit Kiln", cost: 60.00 }
      ],
      labour_hours: 5.5,
      hourly_wage: 120.00,
      overhead_cost: 70.00,
      retail_margin: 0.28,
      b2b_margin: 0.14
    },
    comparable_market: {
      market_range: [1100, 1650],
      commercial_retail_avg: 1450,
      middleman_artisan_share: 25
    },
    b2b_wholesale: {
      moq: 10,
      lead_time_days: 12,
      production_capacity_monthly: 250,
      tiers: [
        { min_qty: 1, max_qty: 9, discount_pct: 0, label: "Retail Single" },
        { min_qty: 10, max_qty: 49, discount_pct: 22, label: "Studio / Boutique" },
        { min_qty: 50, max_qty: 99, discount_pct: 30, label: "Wholesale Distributor" },
        { min_qty: 100, max_qty: 500, discount_pct: 38, label: "Bulk Export Partner" }
      ]
    },
    tags: ["terracotta", "pottery", "clay water pot", "rajasthani", "handmade", "eco-friendly", "cooling matka", "molela"]
  },

  "blue-pottery-vase": {
    id: "item_bp_002",
    craft_type: "Ceramics",
    name: "Jaipur GI Blue Pottery Royal Peacock Vase",
    hindi_name: "जयपुर जीआई ब्लू पॉटरी मयूर नक्काशी फूलदान",
    tagline: "Traditional Clay-Free Glazed Ceramic with Persian Cobalt Pigments",
    category: "Home Decor",
    subcategory: "Vases & Accent Vessels",
    material: "Quartz Powder, Glass, Fuller's Earth, Natural Gum & Cobalt Oxide",
    gi_tagged: true,
    gi_registration_number: "GI-Appl-No-2",
    origin: {
      village: "Kot Jewar",
      district: "Jaipur",
      state: "Rajasthan",
      region: "Northern India"
    },
    artisan: {
      name: "Kripal Singh Rathore",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80",
      experience_years: 31,
      community: "Jaipur Heritage Blue Pottery Collective",
      quote: "Blue pottery contains no clay; it is born from pure quartz crystals and fired with cobalt grace."
    },
    description: "Authentic Geographical Indication (GI) tagged Jaipur Blue Pottery. Crafted using a heritage Indo-Persian dough of powdered quartz, raw glass, katira gond, and multani mitti. Hand-painted with fine squirrel-hair brushes in cobalt blue and turquoise mineral glazes depicting royal peacocks and lotus vines.",
    dimensions: "Height: 32 cm | Rim Diameter: 12 cm | Base: 14 cm",
    weight: "1.85 kg",
    care_instructions: "Wipe with a soft damp microfibre cloth. Fragile; protect against sharp impact. Not suitable for dishwasher.",
    image_url: "https://images.unsplash.com/photo-1612196808214-b8e1d6145a8c?w=800&auto=format&fit=crop&q=80",
    pricing_factors: {
      material_cost: 450.00,
      material_breakdown: [
        { item: "High Purity Quartz Powder & Recycled Glass", cost: 160.00 },
        { item: "Natural Cobalt Oxide & Copper Pigments", cost: 210.00 },
        { item: "Katira Gond Gum & Multani Mitti Binders", cost: 80.00 }
      ],
      labour_hours: 9.0,
      hourly_wage: 150.00,
      overhead_cost: 120.00,
      retail_margin: 0.30,
      b2b_margin: 0.15
    },
    comparable_market: {
      market_range: [2400, 3800],
      commercial_retail_avg: 3200,
      middleman_artisan_share: 22
    },
    b2b_wholesale: {
      moq: 6,
      lead_time_days: 18,
      production_capacity_monthly: 120,
      tiers: [
        { min_qty: 1, max_qty: 5, discount_pct: 0, label: "Retail Single" },
        { min_qty: 6, max_qty: 24, discount_pct: 20, label: "Gallery & Boutique" },
        { min_qty: 25, max_qty: 49, discount_pct: 28, label: "Luxury Interior Retail" },
        { min_qty: 50, max_qty: 200, discount_pct: 36, label: "Hospitality Bulk" }
      ]
    },
    tags: ["blue pottery", "jaipur pottery", "gi tagged", "peacock vase", "ceramics", "hand painted", "rajasthan heritage"]
  },

  "madhubani-canvas": {
    id: "item_mb_003",
    craft_type: "Folk Painting",
    name: "Madhubani 'Tree of Life' Natural Dye Wall Art",
    hindi_name: "मधुबनी हस्तचित्रित 'जीवन वृक्ष' प्राकृतिक कैनवास",
    tagline: "GI-Certified Mithila Art Painted with Bamboo Twigs and Forest Dyes",
    category: "Art & Collectibles",
    subcategory: "Fine Art Paintings",
    material: "Handmade Tussar Cotton Canvas, Lampblack & Botanical Extracts",
    gi_tagged: true,
    gi_registration_number: "GI-Appl-No-45",
    origin: {
      village: "Ranti",
      district: "Madhubani",
      state: "Bihar",
      region: "Eastern India"
    },
    artisan: {
      name: "Sunita Devi Jha",
      avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&auto=format&fit=crop&q=80",
      experience_years: 28,
      community: "Mithila Mahila Kalakar Society",
      quote: "Our brushes are sharpened bamboo twigs; our ink comes from the roots of turmeric and deep lamp soot."
    },
    description: "Authentic Kachni and Bharni style Madhubani painting created on cow-dung treated handmade cotton rag paper. Intricately rendered using sharpened bamboo nibs without preliminary pencil sketches. Pigments are 100% natural, extracted from indigo, turmeric root, parijat flowers, kusum leaves, and pure lampblack soot.",
    dimensions: "45 cm x 60 cm (18 x 24 inches, unframed with 2-inch border)",
    weight: "0.35 kg",
    care_instructions: "Frame under UV-protective museum glass. Keep away from direct high humidity and damp surfaces.",
    image_url: "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
    pricing_factors: {
      material_cost: 310.00,
      material_breakdown: [
        { item: "Organic Cotton-Rag Canvas (Cold Pressed)", cost: 140.00 },
        { item: "Botanical Dyes (Indigo, Turmeric, Kusum)", cost: 110.00 },
        { item: "Bamboo Nibs & Organic Gum Binders", cost: 60.00 }
      ],
      labour_hours: 14.0,
      hourly_wage: 140.00,
      overhead_cost: 90.00,
      retail_margin: 0.28,
      b2b_margin: 0.14
    },
    comparable_market: {
      market_range: [3100, 5200],
      commercial_retail_avg: 4200,
      middleman_artisan_share: 18
    },
    b2b_wholesale: {
      moq: 5,
      lead_time_days: 21,
      production_capacity_monthly: 45,
      tiers: [
        { min_qty: 1, max_qty: 4, discount_pct: 0, label: "Retail Collector" },
        { min_qty: 5, max_qty: 19, discount_pct: 18, label: "Curated Art Galleries" },
        { min_qty: 20, max_qty: 49, discount_pct: 25, label: "Corporate Gifting" },
        { min_qty: 50, max_qty: 100, discount_pct: 32, label: "Museum & Export" }
      ]
    },
    tags: ["madhubani", "mithila art", "tree of life", "gi tagged", "natural dyes", "folk painting", "bihar craft", "handmade"]
  },

  "dhokra-nandi": {
    id: "item_dk_004",
    craft_type: "Metal Craft",
    name: "Bastar Dhokra Lost-Wax Bell Metal Nandi",
    hindi_name: "बस्तर ढोकरा ढलवा पीतल नंदी प्रतिमा",
    tagline: "4000-Year-Old Lost-Wax Bell Metal Cast from the Deep Forests of Bastar",
    category: "Home Decor",
    subcategory: "Sculptures & Heritage Metalware",
    material: "Recycled Brass, Bronze, Beeswax, Damar Resin & Red Clay",
    gi_tagged: true,
    gi_registration_number: "GI-Appl-No-83",
    origin: {
      village: "Kondagaon",
      district: "Bastar",
      state: "Chhattisgarh",
      region: "Central India"
    },
    artisan: {
      name: "Sukhlal Ghadwa",
      avatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80",
      experience_years: 27,
      community: "Bastar Ghadwa Bell Metal Guild",
      quote: "Each wax strand is coiled by thumb; when the furnace glows, the wax departs and metal takes its soul."
    },
    description: "Handmade using the ancient non-ferrous lost-wax casting technique (cire perdue) dating back to the Indus Valley Dancing Girl. Constructed from fine threads of pure forest beeswax coiled over a clay core, encased in termite-mound clay slip, and filled with molten scrap brass and bronze.",
    dimensions: "Length: 19 cm | Width: 9 cm | Height: 16 cm",
    weight: "1.45 kg",
    care_instructions: "Dust with dry cotton cloth. To restore antique warm glow, gently polish with brass polish or tamarind paste.",
    image_url: "https://images.unsplash.com/photo-1590736969955-71cc94801759?w=800&auto=format&fit=crop&q=80",
    pricing_factors: {
      material_cost: 380.00,
      material_breakdown: [
        { item: "Brass & Bronze Bell Metal Alloy (1.8 kg)", cost: 220.00 },
        { item: "Wild Beeswax & Damar Resin", cost: 90.00 },
        { item: "Termite Anthill Clay & Rice Husk Core", cost: 70.00 }
      ],
      labour_hours: 8.5,
      hourly_wage: 130.00,
      overhead_cost: 100.00,
      retail_margin: 0.30,
      b2b_margin: 0.15
    },
    comparable_market: {
      market_range: [2100, 3400],
      commercial_retail_avg: 2800,
      middleman_artisan_share: 24
    },
    b2b_wholesale: {
      moq: 8,
      lead_time_days: 15,
      production_capacity_monthly: 80,
      tiers: [
        { min_qty: 1, max_qty: 7, discount_pct: 0, label: "Retail Single" },
        { min_qty: 8, max_qty: 29, discount_pct: 20, label: "Handicraft Boutiques" },
        { min_qty: 30, max_qty: 74, discount_pct: 28, label: "Architectural Decor" },
        { min_qty: 75, max_qty: 200, discount_pct: 35, label: "Export Supply" }
      ]
    },
    tags: ["dhokra", "bastar art", "bell metal", "lost wax casting", "nandi statue", "brass sculpture", "chhattisgarh", "gi tagged"]
  },

  "banarasi-silk-stole": {
    id: "item_bs_005",
    craft_type: "Handloom Weaving",
    name: "Banarasi Pure Katan Silk Handloom Stole",
    hindi_name: "बनारसी शुद्ध कतान सिल्क हथकरघा स्टोल (दुपट्टा)",
    tagline: "Handwoven with Fine Pure Silk Warp and Intricate Zari Butidar Weft",
    category: "Apparel & Accessories",
    subcategory: "Scarves, Shawls & Stoles",
    material: "100% Pure Mulberry Silk & Electroplated Gold Zari",
    gi_tagged: true,
    gi_registration_number: "GI-Appl-No-99",
    origin: {
      village: "Kotwa",
      district: "Varanasi",
      state: "Uttar Pradesh",
      region: "Northern India"
    },
    artisan: {
      name: "Mohammad Rizwan Ansari",
      avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&auto=format&fit=crop&q=80",
      experience_years: 35,
      community: "Varanasi Bunkar Handloom Weavers Society",
      quote: "The rhythmic clatter of our pit loom weaves centuries of Banaras into every inch of silk."
    },
    description: "Authentic Handloom Mark and Silk Mark certified Banarasi stole. Handwoven on traditional wooden pit looms across 16 days. Embellished with classic shikargah and floral kadhwa zari motifs using pure silk yarns and tested metallic gold threads.",
    dimensions: "Length: 200 cm | Width: 70 cm (78 x 28 inches)",
    weight: "0.22 kg",
    care_instructions: "Dry clean only. Store wrapped in breathable muslin fabric. Do not iron directly on metallic zari.",
    image_url: "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800&auto=format&fit=crop&q=80",
    pricing_factors: {
      material_cost: 980.00,
      material_breakdown: [
        { item: "Pure Mulberry Katan Silk Yarn (350g)", cost: 650.00 },
        { item: "Metallic Electroplated Gold Zari Thread", cost: 220.00 },
        { item: "Natural Dyeing & Finishing Sizing", cost: 110.00 }
      ],
      labour_hours: 16.0,
      hourly_wage: 160.00,
      overhead_cost: 140.00,
      retail_margin: 0.28,
      b2b_margin: 0.14
    },
    comparable_market: {
      market_range: [4800, 7500],
      commercial_retail_avg: 5900,
      middleman_artisan_share: 20
    },
    b2b_wholesale: {
      moq: 6,
      lead_time_days: 25,
      production_capacity_monthly: 60,
      tiers: [
        { min_qty: 1, max_qty: 5, discount_pct: 0, label: "Retail Single" },
        { min_qty: 6, max_qty: 19, discount_pct: 18, label: "Ethnic Boutiques" },
        { min_qty: 20, max_qty: 49, discount_pct: 26, label: "Departmental Stores" },
        { min_qty: 50, max_qty: 150, discount_pct: 34, label: "Fashion Wholesalers" }
      ]
    },
    tags: ["banarasi silk", "katan silk", "handloom", "zari work", "varanasi weaver", "silk mark", "gi tagged", "luxury stole"]
  }
};

// ── 2. STATE ─────────────────────────────────────────────────────────
let activeCraftKey = "terracotta-pot";
let activeMode = "retail"; // "retail" | "b2b"
let retailQuantity = 1;
let b2bQuantity = 10;
let cartCount = 0;

// ── 3. PRICING & CALCULATION ENGINE ─────────────────────────────────
function calculateCostPlus(craft) {
  const pf = craft.pricing_factors;
  const labourCost = pf.labour_hours * pf.hourly_wage;
  const primeCost = pf.material_cost + labourCost;
  const baseCost = primeCost + (pf.overhead_cost || 0);

  const retailPrice = baseCost * (1 + pf.retail_margin);
  const b2bPrice = baseCost * (1 + pf.b2b_margin);

  // Direct artisan earnings = wages + 70% of collective margin
  const artisanProfit = (retailPrice - baseCost) * 0.70;
  const artisanTotalEarnings = labourCost + artisanProfit;
  const artisanSharePct = (artisanTotalEarnings / retailPrice) * 100;

  const marketAvg = craft.comparable_market.commercial_retail_avg;
  const buyerSavingsPct = Math.max(0, ((marketAvg - retailPrice) / marketAvg) * 100);

  // Human-readable "Why this price?" narrative
  const explanation = `Priced fairly at ₹${retailPrice.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })} based on ${pf.labour_hours} hours of skilled craft labour at a guaranteed ethical wage of ₹${pf.hourly_wage}/hr (₹${labourCost.toLocaleString("en-IN")} labour), ₹${pf.material_cost} in authentic raw materials, and a transparent ${Math.round(pf.retail_margin * 100)}% artisan collective margin. The artisan receives ₹${artisanTotalEarnings.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })} (${artisanSharePct.toFixed(1)}% of the retail price), compared to only ~${craft.comparable_market.middleman_artisan_share}% in traditional multi-tier retail channels. Similar ${craft.craft_type.toLowerCase()} items typically retail commercially between ₹${craft.comparable_market.market_range[0].toLocaleString("en-IN")} and ₹${craft.comparable_market.market_range[1].toLocaleString("en-IN")}.`;

  return {
    labourCost,
    primeCost,
    baseCost,
    retailPrice,
    b2bPrice,
    artisanTotalEarnings,
    artisanSharePct,
    marketAvg,
    buyerSavingsPct,
    explanation
  };
}

function calculateB2BVolume(craft, quantity) {
  const calc = calculateCostPlus(craft);
  const tiers = craft.b2b_wholesale.tiers;
  
  let matchedTier = tiers[0];
  for (const t of tiers) {
    if (quantity >= t.min_qty && quantity <= t.max_qty) {
      matchedTier = t;
      break;
    } else if (quantity > t.max_qty) {
      matchedTier = t;
    }
  }

  const discountRate = matchedTier.discount_pct / 100;
  const discountedUnit = calc.retailPrice * (1 - discountRate);
  const unitPrice = Math.max(calc.b2bPrice, discountedUnit);

  const totalAmount = unitPrice * quantity;
  const retailTotal = calc.retailPrice * quantity;
  const totalSavings = Math.max(0, retailTotal - totalAmount);

  return {
    quantity,
    matchedTier,
    retailUnitPrice: calc.retailPrice,
    unitPrice,
    totalAmount,
    retailTotal,
    totalSavings,
    moqMet: quantity >= craft.b2b_wholesale.moq
  };
}

// ── 4. ONDC BECKN SCHEMA GENERATOR ──────────────────────────────────
function generateOndcPayload(craft) {
  const calc = calculateCostPlus(craft);
  const pf = craft.pricing_factors;

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
      "timestamp": new Date().toISOString()
    },
    "message": {
      "catalog": {
        "bpp/descriptor": {
          "name": "Bharat Artisan Direct Marketplace (SIH Workstream 4)",
          "short_desc": "Empowering Rural Artisans via Fair-Wage Cost-Plus Pricing",
          "long_desc": "Open Network for Digital Commerce verified artisan craft catalog with GI tags and transparent fair-wage cost breakdown."
        },
        "bpp/providers": [
          {
            "id": "PROVIDER_BHARAT_ARTISAN_FEDERATION",
            "descriptor": {
              "name": "All India Artisans & Craftworkers Guild"
            },
            "items": [
              {
                "id": craft.id,
                "descriptor": {
                  "name": craft.name,
                  "code": `SKU-${craft.id.toUpperCase()}`,
                  "symbol": craft.image_url,
                  "short_desc": craft.tagline,
                  "long_desc": craft.description,
                  "images": [craft.image_url]
                },
                "price": {
                  "currency": "INR",
                  "value": calc.retailPrice.toFixed(2),
                  "maximum_value": calc.marketAvg.toFixed(2)
                },
                "category_id": craft.category,
                "fulfillment_id": "F1_HANDICRAFT_SECURE_EXPRESS",
                "location_id": `LOC_${craft.origin.state.toUpperCase().slice(0, 4)}`,
                "matched": true,
                "recommended": true,
                "@ondc/org/returnable": false,
                "@ondc/org/cancellable": true,
                "@ondc/org/time_to_ship": `P${craft.b2b_wholesale.lead_time_days}D`,
                "tags": [
                  {
                    "code": "craft_authenticity",
                    "list": [
                      { "code": "craft_type", "value": craft.craft_type },
                      { "code": "gi_tagged", "value": craft.gi_tagged ? "true" : "false" },
                      { "code": "origin_state", "value": craft.origin.state },
                      { "code": "origin_village", "value": craft.origin.village },
                      { "code": "artisan_name", "value": craft.artisan.name },
                      { "code": "artisan_share_pct", "value": `${calc.artisanSharePct.toFixed(1)}%` }
                    ]
                  },
                  {
                    "code": "b2b_wholesale_spec",
                    "list": [
                      { "code": "b2b_unit_price", "value": calc.b2bPrice.toFixed(2) },
                      { "code": "moq", "value": String(craft.b2b_wholesale.moq) },
                      { "code": "production_capacity_monthly", "value": String(craft.b2b_wholesale.production_capacity_monthly) },
                      { "code": "lead_time_days", "value": String(craft.b2b_wholesale.lead_time_days) }
                    ]
                  },
                  {
                    "code": "price_transparency",
                    "list": [
                      { "code": "labour_hours", "value": String(pf.labour_hours) },
                      { "code": "hourly_wage", "value": `INR ${pf.hourly_wage.toFixed(0)}` },
                      { "code": "material_cost", "value": `INR ${pf.material_cost.toFixed(2)}` },
                      { "code": "why_this_price", "value": calc.explanation }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  };
}

// ── 5. UI RENDER FUNCTIONS ───────────────────────────────────────────
function renderCraftChips() {
  const container = document.getElementById("craftChipsList");
  container.innerHTML = "";

  Object.entries(CRAFTS_DATA).forEach(([key, craft]) => {
    const chip = document.createElement("button");
    chip.type = "button";
    chip.className = `craft-chip ${key === activeCraftKey ? "active" : ""}`;
    chip.innerHTML = `
      <span>${craft.name.split(" ")[0]} ${craft.name.split(" ")[1] || ""}</span>
      ${craft.gi_tagged ? '<span class="chip-gi-badge">GI</span>' : ""}
    `;
    chip.addEventListener("click", () => {
      selectCraft(key);
    });
    container.appendChild(chip);
  });
}

function selectCraft(key) {
  if (!CRAFTS_DATA[key]) return;
  activeCraftKey = key;
  const craft = CRAFTS_DATA[key];
  
  // Reset quantities to craft defaults
  retailQuantity = 1;
  b2bQuantity = craft.b2b_wholesale.moq;

  // Update slider bounds & value
  const slider = document.getElementById("b2bQtySlider");
  slider.min = Math.max(5, craft.b2b_wholesale.moq - 5);
  slider.max = craft.b2b_wholesale.tiers[craft.b2b_wholesale.tiers.length - 1].max_qty;
  slider.value = b2bQuantity;

  renderCraftChips();
  renderProductView();
}

function renderProductView() {
  const craft = CRAFTS_DATA[activeCraftKey];
  const calc = calculateCostPlus(craft);

  // 1. Header & Titles
  document.getElementById("catBreadcrumb").textContent = craft.category;
  document.getElementById("subcatBreadcrumb").textContent = craft.subcategory;
  document.getElementById("skuTag").textContent = `SKU-${craft.id.toUpperCase()}`;
  document.getElementById("productTitle").textContent = craft.name;
  document.getElementById("hindiTitle").textContent = craft.hindi_name;
  document.getElementById("productTagline").textContent = craft.tagline;

  // 2. Images & Badges
  document.getElementById("productImage").src = craft.image_url;
  document.getElementById("productImage").alt = craft.name;
  document.getElementById("captionLeadTime").textContent = `Lead Time: ${craft.b2b_wholesale.lead_time_days} days`;
  document.getElementById("captionOrigin").textContent = `${craft.origin.village}, ${craft.origin.state}`;

  const giBadge = document.getElementById("giBadge");
  if (craft.gi_tagged) {
    giBadge.style.display = "inline-flex";
    giBadge.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg> GI Tagged (${craft.gi_registration_number || "Certified"})`;
  } else {
    giBadge.style.display = "none";
  }

  // 3. Artisan Card
  document.getElementById("artisanAvatar").src = craft.artisan.avatar;
  document.getElementById("artisanName").textContent = craft.artisan.name;
  document.getElementById("artisanExp").textContent = craft.artisan.experience_years;
  document.getElementById("artisanCommunity").textContent = craft.artisan.community;
  document.getElementById("artisanQuote").textContent = `"${craft.artisan.quote}"`;

  // 4. Specs Card
  document.getElementById("specDimensions").textContent = craft.dimensions;
  document.getElementById("specWeight").textContent = craft.weight;
  document.getElementById("specMaterial").textContent = craft.material;
  document.getElementById("specCare").textContent = craft.care_instructions;

  // 5. Description & Tags
  document.getElementById("productDescription").textContent = craft.description;
  const tagsContainer = document.getElementById("productTags");
  tagsContainer.innerHTML = "";
  craft.tags.forEach(t => {
    const span = document.createElement("span");
    span.className = "tag-badge";
    span.textContent = `#${t}`;
    tagsContainer.appendChild(span);
  });

  // 6. Retail Panel
  document.getElementById("retailPriceAmount").textContent = calc.retailPrice.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  document.getElementById("marketComparisonMrp").textContent = `MRP ₹${calc.marketAvg.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  document.getElementById("buyerSavingBadge").textContent = `Save ${calc.buyerSavingsPct.toFixed(0)}% vs Commercial`;
  
  document.getElementById("artisanSharePct").textContent = `${calc.artisanSharePct.toFixed(1)}% goes to ${craft.artisan.name.split(" ")[0]}`;
  document.getElementById("impactProgressBar").style.width = `${calc.artisanSharePct}%`;
  document.getElementById("artisanEarningsTotal").textContent = calc.artisanTotalEarnings.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  
  const pf = craft.pricing_factors;
  document.getElementById("whyPriceSnippet").textContent = `Based on ${pf.labour_hours} hrs skilled labour at ₹${pf.hourly_wage}/hr living wage, ₹${pf.material_cost} raw materials, and fair ${Math.round(pf.retail_margin * 100)}% guild margin.`;
  
  document.getElementById("retailQtyInput").value = retailQuantity;
  updateRetailSubtotal();

  // 7. B2B Panel
  document.getElementById("b2bMoqBadge").textContent = `MOQ: ${craft.b2b_wholesale.moq} Units`;
  document.getElementById("b2bBaseUnitPrice").textContent = calc.b2bPrice.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  document.getElementById("b2bStandardRetail").textContent = calc.retailPrice.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  document.getElementById("b2bMonthlyCapacity").textContent = `${craft.b2b_wholesale.production_capacity_monthly} pieces`;
  document.getElementById("b2bLeadTime").textContent = `${craft.b2b_wholesale.lead_time_days} Business Days`;

  renderTierCards();
  updateB2BSimulator();

  // 8. Update Live ONDC JSON
  updateOndcJsonView();
}

function updateRetailSubtotal() {
  const craft = CRAFTS_DATA[activeCraftKey];
  const calc = calculateCostPlus(craft);
  const total = calc.retailPrice * retailQuantity;
  document.getElementById("retailSubtotal").textContent = `₹${total.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

function renderTierCards() {
  const craft = CRAFTS_DATA[activeCraftKey];
  const grid = document.getElementById("tierCardsGrid");
  grid.innerHTML = "";

  craft.b2b_wholesale.tiers.forEach((t, index) => {
    const isMatched = b2bQuantity >= t.min_qty && b2bQuantity <= t.max_qty;
    const card = document.createElement("div");
    card.className = `tier-card ${isMatched ? "active" : ""}`;
    card.innerHTML = `
      <div class="tier-range">${t.min_qty}–${t.max_qty} pcs</div>
      <div class="tier-discount">${t.discount_pct > 0 ? `${t.discount_pct}% OFF` : "Standard"}</div>
      <div class="tier-name">${t.label}</div>
    `;
    card.addEventListener("click", () => {
      b2bQuantity = t.min_qty;
      document.getElementById("b2bQtySlider").value = b2bQuantity;
      updateB2BSimulator();
      renderTierCards();
    });
    grid.appendChild(card);
  });
}

function updateB2BSimulator() {
  const craft = CRAFTS_DATA[activeCraftKey];
  const sim = calculateB2BVolume(craft, b2bQuantity);

  document.getElementById("b2bQtyDisplay").textContent = b2bQuantity;
  document.getElementById("matchedTierBadge").textContent = `${sim.matchedTier.label} (${sim.matchedTier.discount_pct}% Off)`;
  document.getElementById("simUnitPrice").textContent = `₹${sim.unitPrice.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  document.getElementById("simTotalAmount").textContent = `₹${sim.totalAmount.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
  document.getElementById("simSavings").textContent = `₹${sim.totalSavings.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

// ── 6. MODAL & DRAWER CONTROLS ──────────────────────────────────────
function openWhyPriceModal() {
  const craft = CRAFTS_DATA[activeCraftKey];
  const calc = calculateCostPlus(craft);
  const pf = craft.pricing_factors;

  document.getElementById("modalFullExplanation").textContent = calc.explanation;

  // Render cost tree
  const costTree = document.getElementById("modalCostTree");
  costTree.innerHTML = `
    <div class="tree-node">
      <div class="tree-node-header">
        <span>1. Raw Materials & Organic Inputs</span>
        <span>₹${pf.material_cost.toFixed(2)}</span>
      </div>
      <div class="tree-node-sub">
        ${pf.material_breakdown.map(b => `${b.item} (₹${b.cost})`).join(" • ")}
      </div>
    </div>
    <div class="tree-node">
      <div class="tree-node-header">
        <span>2. Skilled Craft Labour (${pf.labour_hours} hrs @ ₹${pf.hourly_wage}/hr)</span>
        <span>₹${calc.labourCost.toFixed(2)}</span>
      </div>
      <div class="tree-node-sub">Benchmarked above statutory living wage standards. Guaranteed direct to artisan.</div>
    </div>
    <div class="tree-node">
      <div class="tree-node-header">
        <span>3. Workshop Overhead & Packaging</span>
        <span>₹${(pf.overhead_cost || 0).toFixed(2)}</span>
      </div>
      <div class="tree-node-sub">Eco-friendly protective packing and kiln/workshop utilities.</div>
    </div>
    <div class="tree-node">
      <div class="tree-node-header">
        <span>4. Artisan Collective Fair Markup (${Math.round(pf.retail_margin * 100)}%)</span>
        <span>₹${((calc.retailPrice - calc.baseCost)).toFixed(2)}</span>
      </div>
      <div class="tree-node-sub">70% routed directly to artisan bonus; 30% to community healthcare & apprentice fund.</div>
    </div>
    <div class="tree-node total">
      <div class="tree-node-header">
        <span>Total Fair Retail Price:</span>
        <span>₹${calc.retailPrice.toFixed(2)}</span>
      </div>
    </div>
  `;

  document.getElementById("compOurArtisanShare").textContent = `${calc.artisanSharePct.toFixed(1)}% to Artisan`;
  document.getElementById("compOurBar").style.width = `${calc.artisanSharePct}%`;
  document.getElementById("compOurPrice").textContent = calc.retailPrice.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  document.getElementById("compMarketPrice").textContent = calc.marketAvg.toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  document.getElementById("modalMarketRange").textContent = `₹${craft.comparable_market.market_range[0].toLocaleString("en-IN")} — ₹${craft.comparable_market.market_range[1].toLocaleString("en-IN")}`;

  document.getElementById("whyPriceModal").classList.remove("hidden");
}

function openPassportModal() {
  const craft = CRAFTS_DATA[activeCraftKey];
  document.getElementById("passTokenId").textContent = `PASSPORT-IND-${craft.origin.state.slice(0,3).toUpperCase()}-2026-${craft.id.toUpperCase()}`;
  document.getElementById("passGiReg").textContent = craft.gi_tagged 
    ? `GI Registration: ${craft.gi_registration_number} (Government of India)` 
    : "Verified Traditional Guild Provenance (Molela Craft Cluster)";
  document.getElementById("passOrigin").textContent = `${craft.origin.village}, ${craft.origin.district}, ${craft.origin.state} (${craft.origin.region})`;
  document.getElementById("passArtisan").textContent = `${craft.artisan.name} (${craft.artisan.experience_years} years master practitioner)`;
  document.getElementById("passMaterials").textContent = craft.material;
  
  document.getElementById("passportModal").classList.remove("hidden");
}

function openOndcDrawer() {
  updateOndcJsonView();
  document.getElementById("ondcDrawer").classList.remove("hidden");
}

function updateOndcJsonView() {
  const craft = CRAFTS_DATA[activeCraftKey];
  const payload = generateOndcPayload(craft);
  document.getElementById("ondcJsonCode").textContent = JSON.stringify(payload, null, 2);
}

function showToast(message, type = "success") {
  const container = document.getElementById("toastContainer");
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `
    <span>${type === "success" ? "✅" : "ℹ️"}</span>
    <span>${message}</span>
  `;
  container.appendChild(toast);
  setTimeout(() => {
    toast.remove();
  }, 3200);
}

function showOrderConfirmation(isB2B = false) {
  const craft = CRAFTS_DATA[activeCraftKey];
  const calc = calculateCostPlus(craft);
  const modal = document.getElementById("orderConfirmModal");

  const title = document.getElementById("orderConfirmTitle");
  const sub = document.getElementById("orderConfirmSub");
  const body = document.getElementById("orderConfirmBody");

  const txnId = `ONDC-TXN-${Date.now().toString().slice(-8)}`;

  if (isB2B) {
    const sim = calculateB2BVolume(craft, b2bQuantity);
    title.textContent = "B2B Proforma Wholesale Quote Generated!";
    sub.textContent = `Proforma Reference: ${txnId}`;
    body.innerHTML = `
      <div style="display:flex; flex-direction:column; gap:12px; font-size:0.9rem;">
        <div style="background:rgba(255,255,255,0.05); padding:14px; border-radius:8px; border:1px solid #334155;">
          <div><strong>Product:</strong> ${craft.name}</div>
          <div><strong>Wholesale Quantity:</strong> ${sim.quantity} units (${sim.matchedTier.label})</div>
          <div><strong>Discounted Unit Price:</strong> ₹${sim.unitPrice.toLocaleString("en-IN", { minimumFractionDigits: 2 })}</div>
          <div><strong>Total Order Value:</strong> <span style="color:#FCD34D; font-weight:700;">₹${sim.totalAmount.toLocaleString("en-IN", { minimumFractionDigits: 2 })}</span></div>
          <div><strong>Wholesale Savings:</strong> <span style="color:#10B981;">₹${sim.totalSavings.toLocaleString("en-IN", { minimumFractionDigits: 2 })}</span></div>
        </div>
        <div style="font-size:0.82rem; color:#94A3B8;">
          📍 Direct Artisan Cluster: ${craft.origin.village}, ${craft.origin.state}<br>
          ⏱️ Production Lead Time: ${craft.b2b_wholesale.lead_time_days} business days.<br>
          🛡️ Payment Terms: 30% Advance via ONDC Escrow, 70% on Dispatch Inspection.
        </div>
      </div>
    `;
  } else {
    const total = calc.retailPrice * retailQuantity;
    title.textContent = "ONDC Direct Order Validated & Placed!";
    sub.textContent = `Beckn Network Order ID: ${txnId}`;
    body.innerHTML = `
      <div style="display:flex; flex-direction:column; gap:12px; font-size:0.9rem;">
        <div style="background:rgba(255,255,255,0.05); padding:14px; border-radius:8px; border:1px solid #334155;">
          <div><strong>Item:</strong> ${craft.name}</div>
          <div><strong>Quantity:</strong> ${retailQuantity} piece(s)</div>
          <div><strong>Amount Paid:</strong> <span style="color:#34D399; font-weight:700;">₹${total.toLocaleString("en-IN", { minimumFractionDigits: 2 })}</span></div>
          <div><strong>Direct to Master ${craft.artisan.name}:</strong> <span style="color:#10B981; font-weight:700;">₹${(calc.artisanTotalEarnings * retailQuantity).toLocaleString("en-IN", { minimumFractionDigits: 2 })} (${calc.artisanSharePct.toFixed(1)}%)</span></div>
        </div>
        <div style="font-size:0.82rem; color:#94A3B8;">
          📦 Dispatch Node: Molela Rural Logistics Hub, Rajasthan.<br>
          🚚 Estimated Delivery: 4–7 business days via ONDC Logistics Network.<br>
          📜 Digital Craft Passport NFT/Token minted to your buyer ID.
        </div>
      </div>
    `;
  }

  modal.classList.remove("hidden");
}

// ── 7. CSV EXPORTER ──────────────────────────────────────────────────
function downloadCatalogCsv() {
  const headers = [
    "Item_ID", "Product_Name", "Craft_Type", "State", "Village", "Artisan_Name",
    "GI_Tagged", "Retail_Price_INR", "B2B_Wholesale_Price_INR", "Comparable_Market_Avg_INR",
    "Artisan_Share_Pct", "Material_Cost_INR", "Labour_Hours", "Hourly_Wage_INR", "B2B_MOQ"
  ];

  const rows = Object.values(CRAFTS_DATA).map(c => {
    const calc = calculateCostPlus(c);
    const pf = c.pricing_factors;
    return [
      c.id,
      `"${c.name}"`,
      c.craft_type,
      c.origin.state,
      c.origin.village,
      `"${c.artisan.name}"`,
      c.gi_tagged ? "Yes" : "No",
      calc.retailPrice.toFixed(2),
      calc.b2bPrice.toFixed(2),
      calc.marketAvg.toFixed(2),
      `${calc.artisanSharePct.toFixed(1)}%`,
      pf.material_cost.toFixed(2),
      pf.labour_hours,
      pf.hourly_wage.toFixed(0),
      c.b2b_wholesale.moq
    ];
  });

  const csvContent = [headers.join(","), ...rows.map(r => r.join(","))].join("\n");
  const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "bharat_artisan_ondc_catalog.csv";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  showToast("Exported ONDC catalog as CSV!");
}

function downloadOndcJson() {
  const craft = CRAFTS_DATA[activeCraftKey];
  const payload = generateOndcPayload(craft);
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `ondc_${craft.id}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  showToast(`Downloaded ONDC JSON for ${craft.id}!`);
}

// ── 8. EVENT LISTENERS INITIALIZATION ────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  // Mode switchers
  const retailBtn = document.getElementById("modeRetailBtn");
  const b2bBtn = document.getElementById("modeB2BBtn");
  const retailPanel = document.getElementById("retailPanel");
  const b2bPanel = document.getElementById("b2bPanel");

  retailBtn.addEventListener("click", () => {
    activeMode = "retail";
    retailBtn.classList.add("active");
    b2bBtn.classList.remove("active");
    retailPanel.classList.remove("hidden");
    b2bPanel.classList.add("hidden");
  });

  b2bBtn.addEventListener("click", () => {
    activeMode = "b2b";
    b2bBtn.classList.add("active");
    retailBtn.classList.remove("active");
    b2bPanel.classList.remove("hidden");
    retailPanel.classList.add("hidden");
  });

  // Quantity controls
  document.getElementById("retailQtyDec").addEventListener("click", () => {
    if (retailQuantity > 1) {
      retailQuantity--;
      document.getElementById("retailQtyInput").value = retailQuantity;
      updateRetailSubtotal();
    }
  });

  document.getElementById("retailQtyInc").addEventListener("click", () => {
    if (retailQuantity < 50) {
      retailQuantity++;
      document.getElementById("retailQtyInput").value = retailQuantity;
      updateRetailSubtotal();
    }
  });

  document.getElementById("retailQtyInput").addEventListener("change", (e) => {
    const val = parseInt(e.target.value, 10);
    if (!isNaN(val) && val >= 1) {
      retailQuantity = Math.min(val, 50);
    } else {
      retailQuantity = 1;
    }
    e.target.value = retailQuantity;
    updateRetailSubtotal();
  });

  // B2B Quantity Slider
  document.getElementById("b2bQtySlider").addEventListener("input", (e) => {
    b2bQuantity = parseInt(e.target.value, 10);
    updateB2BSimulator();
    renderTierCards();
  });

  // Cart & Buy Buttons
  document.getElementById("buyOndcBtn").addEventListener("click", () => {
    showOrderConfirmation(false);
  });

  document.getElementById("addCartBtn").addEventListener("click", () => {
    cartCount += retailQuantity;
    document.getElementById("cartCount").textContent = cartCount;
    showToast(`Added ${retailQuantity} unit(s) to ONDC Cart!`);
  });

  document.getElementById("requestQuoteBtn").addEventListener("click", () => {
    showOrderConfirmation(true);
  });

  document.getElementById("orderSampleBtn").addEventListener("click", () => {
    retailQuantity = 1;
    activeMode = "retail";
    retailBtn.click();
    showToast("Loaded 1 Sample Unit in Retail View!");
  });

  // Modals
  document.getElementById("openWhyPriceModalBtn").addEventListener("click", openWhyPriceModal);
  document.getElementById("closeWhyPriceModalBtn").addEventListener("click", () => {
    document.getElementById("whyPriceModal").classList.add("hidden");
  });
  document.getElementById("modalCloseActionBtn").addEventListener("click", () => {
    document.getElementById("whyPriceModal").classList.add("hidden");
  });

  document.getElementById("openPassportBtn").addEventListener("click", openPassportModal);
  document.getElementById("closePassportModalBtn").addEventListener("click", () => {
    document.getElementById("passportModal").classList.add("hidden");
  });
  document.getElementById("closePassportActionBtn").addEventListener("click", () => {
    document.getElementById("passportModal").classList.add("hidden");
  });

  // ONDC Drawer
  document.getElementById("openOndcDrawerBtn").addEventListener("click", openOndcDrawer);
  document.getElementById("closeOndcDrawerBtn").addEventListener("click", () => {
    document.getElementById("ondcDrawer").classList.add("hidden");
  });

  document.getElementById("copyJsonBtn").addEventListener("click", () => {
    const text = document.getElementById("ondcJsonCode").textContent;
    navigator.clipboard.writeText(text).then(() => {
      showToast("ONDC Beckn JSON copied to clipboard!");
    }).catch(() => {
      showToast("Copied to clipboard!");
    });
  });

  document.getElementById("downloadJsonBtn").addEventListener("click", downloadOndcJson);
  document.getElementById("downloadCsvBtn").addEventListener("click", downloadCatalogCsv);

  // Order confirm modal
  document.getElementById("closeOrderConfirmBtn").addEventListener("click", () => {
    document.getElementById("orderConfirmModal").classList.add("hidden");
  });
  document.getElementById("finishOrderBtn").addEventListener("click", () => {
    document.getElementById("orderConfirmModal").classList.add("hidden");
    showToast("Order transaction recorded!");
  });

  // Initial render
  renderCraftChips();
  renderProductView();
});
