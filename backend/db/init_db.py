from db.session import engine
from db.base import Base
from models import user, khata, product

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
