from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

# Notes
# You can also declare body, path and query parameters, all at the same time.

# The function parameters will be recognized as follows:

# If the parameter is also declared in the path, it will be used as a path parameter.
# If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
# If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.

# the FastAPI app defines a PUT endpoint at the path /items/{item_id} that accepts:
# Path parameter: item_id (int from URL path) 
# Request body: item (Item model with name, price, ...)
# Query parameter: q (str from URL query, an optional string ?q=...)

# EX Usage:
# curl -X PUT "http://127.0.0.1:8000/items/42?q=update" -H "Content-Type: application/json" -d '{"name": "Widget", "price": 9.99}'
# Response:
# {
#   "item_id": 42,
#   "name": "Widget",
#   "price": 19.99,
#   "description": "A test item",
#   "q": "update"
# }