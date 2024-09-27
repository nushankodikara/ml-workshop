from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Usage", description="This is a simple FastAPI use case")

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

items = {}

@app.get("/")
async def read_root():
    return {"Nushan": "Hi!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "item": items.get(item_id)}

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    del items[item_id]
    return {"item_id": item_id, "item": None}
