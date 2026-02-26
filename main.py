from fastapi import FastAPI
from database import engine
import models
from routes.milk import router as milk_router
from routes.farmer import router as farmer_router
from routes.auth_routes import router as auth_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Dairy Management SaaS",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(auth_router)
app.include_router(milk_router)
app.include_router(farmer_router)


@app.get("/")
def root():
    return {"message": "Dairy SaaS Running Successfully"}

