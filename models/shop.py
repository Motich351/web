#аналогично worker.py в main не забудь раскоментировать вызов shop_router
from typing import List
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from database import Shop


ShopOut = sqlalchemy_to_pydantic(Shop)


class ShopIn(sqlalchemy_to_pydantic(Shop)):
    class Config:
        orm_mode = True


class ShopsOut(BaseModel):
    shops: List[ShopOut]
