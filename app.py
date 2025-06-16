from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int
    description: Optional[str] = None

items: Dict[str, Item] = {}

@app.get("/")
def root():
    return {"message": "Advanced REST API"}

@app.get("/items")
def list_items():
    return items

@app.get("/items/{item_name}")
def get_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_name]

@app.post("/items/")
def create_item(item: Item):
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return {"message": "Item created successfully", "item": item}

@app.put("/items/{item_name}")
def update_item(item_name: str, item: Item):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_name] = item
    return {"message": "Item updated successfully", "item": item}

@app.delete("/items/{item_name}")
def delete_item(item_name: str):
    if item_name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_name]
    return {"message": "Item deleted successfully"}

@app.get("/search/")
def search_item(min_price: Optional[float] = None, max_price: Optional[float] = None):
    result = {}
    for name, item in items.items():
        if ((min_price is None or item.price >= min_price) and
            (max_price is None or item.price <= max_price)):
            result[name] = item
    return result
