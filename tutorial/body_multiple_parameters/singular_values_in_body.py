# The same way there is a Query and Path to define extra data 
# for query and path parameters, FastAPI provides an equivalent Body.

# For example, extending the previous model, you could decide that 
# you want to have another key importance in the same body, besides the item and user.

# If you declare it as is, because it is a singular value, FastAPI will 
# assume that it is a query parameter.

# But you can instruct FastAPI to treat it as another body key using Body:
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

# Because importance is a singular value, FastAPI would normally assume it is a query parameter,
# but by using Body() it will know that it should be in the body, and it will expect a body like:
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     },
#     "importance": 5
# }
# Again, it will convert the data types, validate, document, etc.

