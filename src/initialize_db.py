from sqlalchemy import create_engine
from models import Base

DATABASE_URI = 'sqlite:///calories_tracker.db' 
engine = create_engine(DATABASE_URI)

# Create tables
Base.metadata.create_all(engine)
