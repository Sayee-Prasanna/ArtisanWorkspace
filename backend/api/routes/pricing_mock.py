from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PricingRequest(BaseModel):
    material_cost: float
    labour_hours: float
    hourly_wage: float
    craft_type: str

@router.post("/calculate")
def calculate_pricing(req: PricingRequest):
    return {
        "retail_price": 1250.00,
        "b2b_price": 950.00,
        "market_range": [1000, 1500],
        "explanation": "Based on 5 hours of labour at ₹100/hr, ₹200 materials, and standard 30% margin. Similar terracotta items retail between ₹1000 and ₹1500."
    }
