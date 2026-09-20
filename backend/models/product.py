from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db.base import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    artisan_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, index=True)
    description = Column(String)
    retail_price = Column(Float)
    b2b_price = Column(Float)
    craft_type = Column(String)
    material = Column(String)
    image_url = Column(String)
