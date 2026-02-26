from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)


class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    village = Column(String)

    milk_entries = relationship("Milk", back_populates="farmer")


class Milk(Base):
    __tablename__ = "milk"

    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"))
    quantity = Column(Float)
    fat = Column(Float)
    snf = Column(Float)
    rate = Column(Float)
    total_amount = Column(Float)
    date = Column(Date)

    farmer = relationship("Farmer", back_populates="milk_entries")