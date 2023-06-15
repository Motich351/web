from sqlalchemy import Column,Integer, CHAR, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Shop(Base):
    __tablename__ = 'shop'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    address = Column(CHAR)
    income = Column(Integer)

    products = relationship('ShopProduct', back_populates='shop')

