from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import ShopProduct

ShopProductOut = sqlalchemy_to_pydantic(ShopProduct)


class ShopProductIn(sqlalchemy_to_pydantic(ShopProduct)):
    class Config:
        orm_mode = True


class ShopProductsOut(BaseModel):
    shop_products: List[ShopProductOut]