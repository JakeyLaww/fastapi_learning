# With Query and Path (and others you'll see later) 
# you can declare number constraints.

# Here, with ge=1, item_id will need to be an integer number 
# "greater than or equal" to 1.

# Note, there is:
# - ge: greater than or equal
# - gt: greater than
# - le: less than or equal
# - lt: less than

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results