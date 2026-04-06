# You can add more information about the parameter.

# That information will be included in the generated OpenAPI 
# and used by the documentation user interfaces and external tools.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string", # You can add a title to the parameter, which will be used in the documentation.
            description="Query string for the items to search in the database that have a good match", # You can add a description
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results