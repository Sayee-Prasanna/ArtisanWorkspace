from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from db.base import Base

class KhataEntry(Base):
    __tablename__ = "khata_entries"
    id = Column(Integer, primary_key=True, index=True)
    artisan_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String) # "income" or "expense"
    amount = Column(Float)
    category = Column(String)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
