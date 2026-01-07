from app.db.config import engine, Base
from app.models import *  # Import all models to register them

def create_tables():
    """Create all database tables"""
    if engine:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully")
    else:
        print("❌ Database not configured - cannot create tables")

if __name__ == "__main__":
    create_tables()
