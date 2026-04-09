# Here's a small trick that can be handy, but you won't need it often.

# If you want to:

# declare the q query parameter without a Query nor any default value
# declare the path parameter item_id using Path
# have them in a different order
# not use Annotated
# ...Python has a little special syntax for that.

# Pass *, as the first parameter of the function.

# Python won't do anything with that *, but it will know that all the
#  following parameters should be called as keyword arguments 
#  (key-value pairs), also known as kwargs. Even if they don't have a default value.

# Only important if you don't use Annotated, because if you use Annotated, 
# the order of the parameters doesn't matter, we can do:

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results