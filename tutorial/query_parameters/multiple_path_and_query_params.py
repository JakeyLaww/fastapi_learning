from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Notes
# You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
# And you don't have to declare them in any specific order.
# They will be detected by name

# EX:
# http://127.0.0.1:8000/users/42/items/widget?q=searchtext&short=true
# so user_id=42, item_id=widget, q=searchtext, short=true

