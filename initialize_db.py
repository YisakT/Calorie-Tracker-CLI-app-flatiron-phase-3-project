from sqlalchemy import create_engine
from models import Base
import config

engine = create_engine(config.DATABASE_URL)
Base.metadata.create_all(engine)
