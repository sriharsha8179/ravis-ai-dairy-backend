from pydantic import BaseModel
from datetime import date


# -------- AUTH --------

class UserCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# -------- Farmer --------

class FarmerCreate(BaseModel):
    name: str
    phone: str
    village: str


class FarmerResponse(FarmerCreate):
    id: int

    class Config:
        orm_mode = True


# -------- Milk --------

class MilkCreate(BaseModel):
    farmer_id: int
    quantity: float
    fat: float
    snf: float
    date: date


class MilkResponse(BaseModel):
    id: int
    farmer_id: int
    quantity: float
    fat: float
    snf: float
    rate: float
    total_amount: float
    date: date

    class Config:
        orm_mode = True