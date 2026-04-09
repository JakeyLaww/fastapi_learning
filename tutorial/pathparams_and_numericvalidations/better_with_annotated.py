# Keep in mind that if you use Annotated, 
# as you are not using function parameter default values, 
# you won't have this problem, 
# and you probably won't need to use *

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results