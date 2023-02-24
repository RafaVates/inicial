from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

app.post("/items/")
def create_item(item: Item):
    return item 