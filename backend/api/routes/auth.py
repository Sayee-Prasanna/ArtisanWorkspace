from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from models.user import User
from core.security import create_access_token
from pydantic import BaseModel

router = APIRouter()

class LoginMock(BaseModel):
    username: str

@router.post("/login")
def login_mock(data: LoginMock, db: Session = Depends(get_db)):
    # Very simple mock login for CLI first phase
    user = db.query(User).filter(User.username == data.username).first()
    if not user:
        user = User(username=data.username, full_name=data.username, role="artisan")
        db.add(user)
        db.commit()
        db.refresh(user)
    
    access_token = create_access_token(subject=user.id)
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id}
