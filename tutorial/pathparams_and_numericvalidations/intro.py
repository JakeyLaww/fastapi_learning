# In the same way that you can declare more validations and metadata 
# for query parameters with Query, you can declare the same type of validations 
# and metadata for path parameters with Path

from typing import Annotated
# Now we import Path() as we did with Query()
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    # we can declare all the same parameters as we did with Query()
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results