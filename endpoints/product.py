from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import ProductIn, ProductOut
from database import get_session, Product
from models.product import ProductsOut

router = APIRouter(prefix="/product", tags=["product"])


@router.get("/get", response_model=ProductOut)
async def get_one(product_id: int, session: Session = Depends(get_session)):
    product: Product = session.query(Product).get(product_id)
    if product:
        product_dto = ProductOut(**product.__dict__)
        return product_dto
    else:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found!")


@router.get("/get_all", response_model=ProductsOut)
async def get_all():
    session = get_session()
    products = session.query(Product).all()
    products_dto = [ProductOut(**product.__dict__) for product in products]
    return ProductsOut(products=products_dto)


@router.post("/create_product", response_model=ProductOut)
async def create_product(product: ProductIn):
    session = get_session()
    orm_product = Product(**product.dict())
    session.add(orm_product)
    session.commit()
    product_dto = ProductOut(**orm_product.__dict__)
    return product_dto


@router.delete("/delete_product/{product_id}", response_model=ProductOut)
async def delete_product(product_id: int, session: Session = Depends(get_session)):
    product: Product = session.query(Product).get(product_id)
    if product:
        product_dto = ProductOut(**product.__dict__)
        session.delete(product)
        session.commit()
        return product_dto
    else:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found!")


@router.post("/update_product", response_model=ProductOut)
async def update_product(product: ProductIn):
    session = get_session()

    orm_product = session.query(Product).get(product.product_id)
    orm_product.name = product.name
    orm_product.price = product.price
    orm_product.numb = product.numb

    session.commit()
    product_dto = ProductOut.from_orm(orm_product)
    return product_dto
