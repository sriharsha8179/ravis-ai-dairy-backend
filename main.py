from fastapi import FastAPI
from database import engine
import models
from milk import router as milk_router
from farmer import router as farmer_router
from auth import router as auth_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dairy Management SaaS")

app.include_router(auth_router)
app.include_router(milk_router)
app.include_router(farmer_router)


@app.get("/")
def root():
    return {"message": "Dairy SaaS Running Successfully"}
