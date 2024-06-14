from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///customers.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base.metadata.create_all(engine)
