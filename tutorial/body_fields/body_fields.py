# The same way you can declare additional validation and metadata 
# in path operation function parameters with Query, Path and Body, 
# you can declare validation and metadata inside of Pydantic models 
# using Pydantic's Field.

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Before, you could declare a Pydantic model like this:
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
# We could declare the fields and their types, and also set default values, but we couldn't declare any additional validation or metadata.
# Now, with Field(), you can declare additional validation and metadata for each field in the P

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# Note:
# item_id -> path parameter
# item -> body parameter, which is a Pydantic model with validation and metadata declared using Field.
# Field works the same way as Query, Path and Body, it has all the same parameters, etc.

