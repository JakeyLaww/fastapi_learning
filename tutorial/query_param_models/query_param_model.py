# Declare the query parameters that you need in a Pydantic model, 
# and then declare the parameter as Query

# Literal is a type hint that allows you to declare that a 
# value must be one of a limited set of values.
from typing import Annotated, Literal

from fastapi import FastAPI, Query

# Field is a Pydantic function used to add validation rules directly to class variables ("gt 0")
from pydantic import BaseModel, Field

app = FastAPI()

# Defines a Pydantic model with the query parameters you want to receive, see request_body/ for a refresher
class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100) # An int query param (0 < limit <= 100) with a default value of 100
    offset: int = Field(0, ge=0) # An int query param (offset >= 0) with a default value of 0
    order_by: Literal["created_at", "updated_at"] = "created_at" # A query param that must be either "created_at" or "updated_at", with a default value of "created_at"
    tags: list[str] = [] # A query param that is a list of strings, with a default value of an empty list


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

# filter_query is the name of the variable inside the function that will receive the data from the query parameters.
# Annotated is used to declare that filter_query is of type FilterParams and that it should be extracted from the query parameters using Query().
# Normally FastAPI would expect filter_query to be a body parameter, but with the use of Query() it knows to look for the data in the query parameters instead.

# Since the BaseModel is a Query(), our URL might look like:
#http://127.0.0.1:8000/items/?limit=20&offset=10&order_by=updated_at&tags=electronics&tags=sale

# FastAPI will extract the data for each field from the query parameters 
# in the request and give you the Pydantic model you defined.