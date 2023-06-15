import uvicorn
from fastapi import FastAPI
from endpoints import worker_router


app = FastAPI()
app.include_router(worker_router)
# app.include_router(shop_router)
# app.include_router(product_router)
# app.include_router(shop_product_router)
if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                log_level="info",
                reload=True)