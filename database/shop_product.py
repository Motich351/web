from sqlalchemy import Column, ForeignKey
from .base_meta import Base
from sqlalchemy.orm import relationship


class ShopProduct(Base):
    __tablename__ = 'shop_product'
    __table_args__ = {'extend_existing': True}

    shop_id = Column(ForeignKey('shop.id'), primary_key=True)
    product_id = Column(ForeignKey('product.id'), primary_key=True)

    shop = relationship("Shop", back_populates="products")
    product = relationship("Product", back_populates="shops")
