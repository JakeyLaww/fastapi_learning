from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# You can also declare bool types, and they will be converted.
# In this case, if you go to:

# http://127.0.0.1:8000/items/foo?short=1
# or
# http://127.0.0.1:8000/items/foo?short=True
# or
# http://127.0.0.1:8000/items/foo?short=true
# or 
# http://127.0.0.1:8000/items/foo?short=on
# or 
# http://127.0.0.1:8000/items/foo?short=yes
# or any other case variation (uppercase, first letter in uppercase, etc), 
# your function will see the parameter short with a bool value of True. Otherwise as False.