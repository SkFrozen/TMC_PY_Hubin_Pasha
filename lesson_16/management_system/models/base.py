from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql://pasha:123@127.0.0.1:5432/master")

Base = declarative_base()
