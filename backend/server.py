import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI(title="AURA GOLD API", version="1.0")

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "aura_gold")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

@app.get("/")
async def root():
    return {"message": "AURA GOLD API is running", "version": "1.0"}

@app.get("/api/products")
async def get_products(category: Optional[str] = None):
    query = {}
    if category and category != "All":
        query["category"] = category
    products = await db.products.find(query).to_list(100)
    for p in products:
        p["_id"] = str(p["_id"])
    return products

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    customer_name: str
    email: str
    phone: str
    address: str
    city: str
    payment_method: str
    items: List[OrderItem]
    total_amount: float

@app.post("/api/orders")
async def create_order(order: OrderCreate):
    order_dict = order.dict()
    order_dict["status"] = "pending"
    result = await db.orders.insert_one(order_dict)
    return {"order_id": str(result.inserted_id), "status": "success", "message": "Order placed successfully!"}
