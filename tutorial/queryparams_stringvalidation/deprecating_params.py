# Now let's say you don't like this parameter anymore.

# You have to leave it there a while because there are clients using it, 
# but you want the docs to clearly show it as deprecated.

# Then pass the parameter deprecated=True to Query

# Note:
# A deprecated query in FastAPI refers to a query parameter (or an entire path operation) 
# that is marked as outdated in the code, signaling to developers that it should no longer 
# be used and will be removed in a future version.
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results