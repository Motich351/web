from sqlalchemy import Column,Integer, CHAR, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(CHAR)
    price = Column(Integer)
    numb = Column(Integer)

    shops = relationship('ShopProduct', back_populates='product')

