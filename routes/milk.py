from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
import models, schemas
from auth import get_current_user
from sqlalchemy import func

router = APIRouter(prefix="/milk", tags=["Milk"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add", response_model=schemas.MilkResponse)
def add_milk(entry: schemas.MilkCreate,
             db: Session = Depends(get_db),
             user=Depends(get_current_user)):

    rate = (entry.fat * 10) + (entry.snf * 5)
    total_amount = entry.quantity * rate

    new_entry = models.Milk(
        farmer_id=entry.farmer_id,
        quantity=entry.quantity,
        fat=entry.fat,
        snf=entry.snf,
        rate=rate,
        total_amount=total_amount,
        date=entry.date
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry


@router.get("/date-wise-summary")
def date_summary(db: Session = Depends(get_db),
                 user=Depends(get_current_user)):

    result = db.query(
        models.Milk.date,
        func.sum(models.Milk.quantity).label("total_quantity"),
        func.sum(models.Milk.total_amount).label("total_revenue")
    ).group_by(models.Milk.date).all()

    return result


@router.get("/payment-summary/{farmer_id}")
def payment_summary(farmer_id: int,
                    db: Session = Depends(get_db),
                    user=Depends(get_current_user)):

    total = db.query(
        func.sum(models.Milk.total_amount)
    ).filter(models.Milk.farmer_id == farmer_id).scalar()

    return {
        "farmer_id": farmer_id,
        "total_payment": total or 0
    }