from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from models.khata import KhataEntry
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class KhataEntryCreate(BaseModel):
    artisan_id: str
    type: str
    amount: float
    category: str
    notes: Optional[str] = None

@router.post("/entry")
def create_entry(entry: KhataEntryCreate, db: Session = Depends(get_db)):
    # Mocking behavior
    new_entry = KhataEntry(
        artisan_id=int(entry.artisan_id),
        type=entry.type,
        amount=entry.amount,
        category=entry.category,
        notes=entry.notes
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    
    # Calculate mock balance and summary
    balance = 15400.00 + entry.amount if entry.type == "income" else 15400.00 - entry.amount
    return {
        "entry_id": f"txn_{new_entry.id}",
        "status": "recorded",
        "current_balance": balance,
        "summary": f"{entry.type.capitalize()} recorded. Total {entry.type} this month updated."
    }
