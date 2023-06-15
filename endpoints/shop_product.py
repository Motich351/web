from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import ShopProductOut, ShopProductIn
from database import get_session, ShopProduct, Product, Shop
from models.shop_product import ShopProductsOut

router = APIRouter(prefix="/shop_product", tags=["shop_product"])


@router.get("/get", response_model=ShopProductOut)
async def get_one(product_id: int, shop_id: int,
                  session: Session = Depends(get_session)):
    shop_product: ShopProduct = session.query(ShopProduct).get((shop_id, product_id))
    if shop_product:
        if shop_product.product_id == product_id:
            shop_product_dto = ShopProductOut(**shop_product.__dict__)
            return shop_product_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Shop with id {shop_id} not found!")


@router.get("/get_all", response_model=ShopProductsOut)
async def get_all():
    session = get_session()
    shop_products: ShopProduct = session.query(ShopProduct).all()
    shop_product_dto = list(map(lambda shop_product: ShopProductOut(**shop_product.__dict__), shop_products))
    return ShopProductsOut(shop_products=shop_product_dto)


@router.post("/create_shop_product", response_model=ShopProductOut)
async def create_shop_product(shop_product: ShopProductIn):
    session = get_session()
    orm_shop_product = ShopProduct(**shop_product.dict())
    id_ = shop_product.product_id
    prod = session.query(Product).get(id_)
    orm_shop_product.product_price = prod.price
    session.add(orm_shop_product)
    session.commit()
    shop_product_dto = ShopProductOut(**orm_shop_product.__dict__)
    return shop_product_dto


@router.post("/update_shop_product", response_model=ShopProductOut)
async def update_shop_product(shop_product: ShopProductIn):
    session = get_session()

    orm_shop_product = session.query(ShopProduct).get((shop_product.shop_id,shop_product.product_id))
    #orm_shop_product.product_count = shop_product.product_count
    id_ = shop_product.product_id
    prod = session.query(Product).get(id_)
    orm_shop_product.product_price = prod.price
    session.commit()
    shop_product_dto = ShopProductOut.from_orm(orm_shop_product)
    return shop_product_dto


@router.delete("/delete_shop_product/{shop_id}/{product_id}", response_model=ShopProductOut)
async def delete_shop_product(shop_id: int,product_id: int , session: Session = Depends(get_session)):
    shop_product: ShopProduct = session.query(ShopProduct).get((shop_id, product_id))
    if shop_product:
        shop_product_dto = ShopProductOut(**shop_product.__dict__)
        session.delete(shop_product)
        session.commit()
        return shop_product_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Order with id {shop_id} not found!")

