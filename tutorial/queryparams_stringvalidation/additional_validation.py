# We are going to enforce that even though q is optional, whenever it is provided, 
# q's length doesn't exceed 50 characters.

# In Python Types Notes, we saw that "Annotated" can be used to add metadata to your parameters
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
# q: str | None  = None does the same thing, but we add addtional metadata to q. 
# Having Query(max_length=50) means that q's length must be at most 50 characters and FastAPI will validate that for us.
# Note we use Query() because it is a query parameter. We'll see more like Path(), Body(), Header(), Cookie(). 

# To make the default value "john" we would write: "q: Annotated[str, Query(max_length=50)] = "john")"
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
# Note: there are other versions of how to do this.
# FastAPI will now:

# Validate the data making sure that the max length is 50 characters
# Show a clear error for the client when the data is not valid
# Document the parameter in the OpenAPI schema path operation (so it will show up in the automatic docs UI)