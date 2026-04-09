# Let's say you only have a single item body parameter from a 
# Pydantic model Item.

# By default, FastAPI will then expect its body directly.

# But if you want it to expect a JSON with a KEY item and 
# inside of it the model contents, as it does when you declare 
# extra body parameters, you can use the special Body parameter embed:
# item: Item = Body(embed=True)

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# Now, the body of the request should be a JSON with a key item and
# inside of it the model contents, as it does when you declare extra body parameters.
# For example, the body of the request should be:
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }
# instead of:
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }