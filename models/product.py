from typing import List
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from database import Product


ProductOut = sqlalchemy_to_pydantic(Product)


class ProductIn(sqlalchemy_to_pydantic(Product)):
    class Config:
        orm_mode = True


class ProductsOut(BaseModel):
    products: List[ProductOut]
