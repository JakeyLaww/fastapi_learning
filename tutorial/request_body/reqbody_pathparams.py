from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # item.model_dump() is a Pydantic method that converts Item model into a dict: {"name": "Widget", "price":...}
    # **item.model_dump() unpacks that dict key-value pairs into a new dict: {"item_id": item_id, "name": "Widget", "price":...}
    return {"item_id": item_id, **item.model_dump()}

# Notes
# This is a PUT endpoint that updates an item by ID, 
# combining a path parameter (item_id) and a request body (Item model).

# EX:
# curl -X PUT "http://127.0.0.1/8000/items/42" -H "Content-Type: application/json" -d '{"name": "Widget", "price": 9.99}'
# Response:
# {
#     "item_id": 42,
#     "name": "Widget",
#     "description": null,
#     "price": 9.99,
#     "tax": null
# }z