from pydantic import BaseModel
from typing import List

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductResponse(ProductCreate):
    id: int
    class Config:
        orm_mode = True

class CartResponse(BaseModel):
    id: int
    products: List[ProductResponse]
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    product_ids: List[int]

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total: float
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
