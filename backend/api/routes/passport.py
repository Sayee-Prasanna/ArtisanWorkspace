from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.orm import Session
from api.deps import get_db
from models.product import Product
import qrcode
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/{product_id}", response_class=HTMLResponse)
def get_passport(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        # Mock product if it doesn't exist just for the demo
        product = Product(
            id=product_id, title="Handcrafted Terracotta Clay Pot", description="Authentic handcrafted terracotta pot perfect for home decor.",
            retail_price=1250.00, b2b_price=950.00, craft_type="Pottery", material="Terracotta"
        )
    
    html_content = f"""
    <html>
        <head>
            <title>Craft Passport: {product.title}</title>
            <style>
                body {{ font-family: sans-serif; padding: 20px; }}
                .card {{ border: 1px solid #ccc; padding: 20px; border-radius: 8px; max-width: 400px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>{product.title}</h2>
                <p><strong>Craft Type:</strong> {product.craft_type}</p>
                <p><strong>Material:</strong> {product.material}</p>
                <p><strong>Retail Price:</strong> ₹{product.retail_price}</p>
                <p>{product.description}</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@router.get("/{product_id}/qr")
def generate_qr(product_id: int, request: Request):
    # Base URL to point to the passport page
    base_url = str(request.base_url)
    product_url = f"{base_url}api/passport/{product_id}"
    
    qr_filename = f"{UPLOAD_DIR}/qr_{product_id}.png"
    
    if not os.path.exists(qr_filename):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(product_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_filename)
        
    return FileResponse(qr_filename, media_type="image/png")
