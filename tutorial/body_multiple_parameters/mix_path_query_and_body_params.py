# First, of course, you can mix Path, Query and request body 
# parameter declarations freely and FastAPI will know what to do.

# And you can also declare body parameters as optional, 
# by setting the default to None

from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# In this example, 
# item_id is a required path parameter, 
# q is an optional query parameter, 
# and item is an optional body parameter.

# In this example, the path operations would
# expect a JSON body with the attributes of an Item, like:
# {
#     "name": "Foo",
#     "description": "A very nice Item",
#     "price": 35.4,        
#     "tax": 3.2,
# }

# You can test this with:
# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/42?q=urgent' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "Smartphone",
#   "description": "A high-end device",
#   "price": 999.99,
#   "tax": 80.0
# }'