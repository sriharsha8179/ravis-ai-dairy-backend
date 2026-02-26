from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/farmers", tags=["Farmers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add", response_model=schemas.FarmerResponse)
def add_farmer(farmer: schemas.FarmerCreate, db: Session = Depends(get_db)):
    new_farmer = models.Farmer(**farmer.dict())
    db.add(new_farmer)
    db.commit()
    db.refresh(new_farmer)
    return new_farmer


@router.get("/", response_model=List[schemas.FarmerResponse])
def get_farmers(db: Session = Depends(get_db)):
    return db.query(models.Farmer).all()