#аналогично worker.py в main не забудь раскоментировать вызов shop_router
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import ShopIn, ShopOut
from database import get_session, Shop
from models.shop import ShopsOut

router = APIRouter(prefix="/shop", tags=["shop"])


@router.get("/get", response_model=ShopOut)
async def get_one(shop_id: int,
                  session: Session = Depends(get_session)):
    shop: Shop = session.query(Shop).get(shop_id)
    if shop:
        shop_dto = ShopOut(**shop.__dict__)
        return shop_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Shop with id {shop_id} not found!")


@router.get("/get_all", response_model=ShopsOut)
async def get_all():
    session = get_session()
    shops = session.query(Shop).all()
    shops_dto = list(map(lambda shop: ShopOut(**shop.__dict__), shops))
    return ShopsOut(shops=shops_dto)


@router.post("/create_shop", response_model=ShopOut)
async def create_shop(shop: ShopIn):
    session = get_session()
    orm_shop = Shop(**shop.dict())
    session.add(orm_shop)
    print(orm_shop.__dict__)
    session.commit()
    print(orm_shop.__dict__)
    shop_dto = ShopOut(**orm_shop.__dict__)
    return shop_dto


@router.delete("/delete_shop/{shop_id}", response_model=ShopOut)
async def delete_shop(shop_id: int, session: Session = Depends(get_session)):
    shop: Shop = session.query(Shop).get(shop_id)
    if shop:
        shop_dto = ShopOut(**shop.__dict__)
        session.delete(shop)
        session.commit()
        return shop_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Shop with id {shop_id} not found!")


@router.post("/update_shop", response_model=ShopOut)
async def update_shop(shop: ShopIn):
    session = get_session()

    orm_shop = session.query(Shop).get(shop.shop_id)
    #session.add(orm_shop)
    orm_shop.address = shop.address
    orm_shop.income = shop.income

    print(orm_shop.__dict__)
    session.commit()
    shop_dto = ShopOut.from_orm(orm_shop)
    return shop_dto
