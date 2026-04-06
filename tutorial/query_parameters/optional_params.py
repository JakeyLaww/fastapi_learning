from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Notes
# The same way, you can declare optional query parameters, by setting their default to None
# In this case, the function parameter q will be optional, and will be None by default.

# You can update q with a query parameter, like http://127.0.0.1:8000/items/5?q=hello