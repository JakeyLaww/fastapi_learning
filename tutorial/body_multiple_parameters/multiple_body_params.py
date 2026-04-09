# you can also declare multiple body parameters, e.g. item and user
from fastapi import FastAPI
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
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

# In this case, FastAPI will notice that there is more than one body parameter 
# in the function (there are two parameters that are Pydantic models).

# So, it will then use the parameter names as keys (field names) 
# in the body, and expect a body like:
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
#     }
# }

# Notice that even though the item was declared the same way as before, 
# it is now expected to be inside of the body with a key item.

# FastAPI will do the automatic conversion from the request, so that the parameter 
# item receives its specific content and the same for user.

# It will perform the validation of the compound data, 
# and will document it like that for the OpenAPI schema and automatic docs.