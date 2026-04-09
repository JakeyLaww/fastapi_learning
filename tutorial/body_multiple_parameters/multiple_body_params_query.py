# Of course, you can also declare additional query 
# parameters whenever you need, additional to any body parameters.

# As, by default, singular values are interpreted as 
# query parameters, you don't have to explicitly add a Query, you can just do:
# q: str | None = None
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic models
# Tells FastAPI what keys and values to look for in JSON bodies
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}") # item_id is a path parameter
async def update_item(
    *, # Python marker to indicate that all following parameters must be specified as keyword arguments (item=101 instead of 101)
    item_id: int, # path parameter
    item: Item, # body parameter
    user: User, # body parameter
    importance: Annotated[int, Body(gt=0)], # body parameter with validation
    q: str | None = None, # query parameter with default value of None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

# EX: 
# curl -X 'PUT' \
#   'http://localhost:8000/items/42?q=hello' \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "item": {
#       "name": "Foo",
#       "description": "The pretender",
#       "price": 42.0,
#       "tax": 3.2
#     },
#     "user": {
#       "username": "dave",
#       "full_name": "Dave Grohl"
#     },
#     "importance": 5
#   }'