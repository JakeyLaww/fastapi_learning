from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# In this case, there are 3 query parameters:

# needy, a required str.
# skip, an int with a default value of 0.
# limit, an optional int.

# Notes
# When you declare a default value for non-path parameters 
# (for now, we have only seen query parameters), then it is not required.

# If you don't want to add a specific value but just make it optional, 
# set the default as None.

# But when you want to make a query parameter required, 
# you can just not declare any default value

# Here the query parameter needy is a required query parameter of type str