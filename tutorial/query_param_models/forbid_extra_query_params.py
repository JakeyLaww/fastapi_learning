# In some special use cases (probably not very common), 
# you might want to restrict the query parameters that you want to receive.

# You can use Pydantic's model configuration to forbid any extra fields:

from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

# Notes:
#If a client tries to send some extra data in the query parameters, 
# they will receive an error response.

# For example, if the client tries to send a tool query parameter 
#with a value of plumbus, like:
# https://example.com/items/?limit=10&tool=plumbus

# They will receive an error response telling them that the query 
# parameter tool is not allowed:
# {
#     "detail": [
#         {
#             "type": "extra_forbidden",
#             "loc": ["query", "tool"],
#             "msg": "Extra inputs are not permitted",
#             "input": "plumbus"
#         }
#     ]
# }