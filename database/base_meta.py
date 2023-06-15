import sqlalchemy.ext.declarative as dec
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import DATABASE_PATH

Base = dec.declarative_base()
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
session_factory = sessionmaker(bind=engine,
                               expire_on_commit=False)


def get_session() -> Session:
    return session_factory()