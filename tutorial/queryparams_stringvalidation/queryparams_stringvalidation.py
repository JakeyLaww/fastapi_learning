from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# FastAPI allows you to declare additional information and validation for your parameters
# The query parameter q is of type str | None, that means that it's of type str but could also be None, 
# and indeed, the default value is None, so FastAPI will know it's not required.