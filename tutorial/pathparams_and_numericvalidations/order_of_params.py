# Let's say that you want to declare the 
# query parameter q as a required str.

# And you don't need to declare anything else for that parameter, 
# so you don't really need to use Query.

# But you still need to use Path for the item_id path parameter. 
# And you don't want to use Annotated for some reason.

# Python will complain if you put a value with a "default" 
# before a value that doesn't have a "default".

# But you can re-order them, and have the value without a 
# default (the query parameter q) first.

# It doesn't matter for FastAPI. It will detect the parameters 
# by their names, types and default declarations (Query, Path, etc), 
# it doesn't care about the order.

# Note this is importatnt if you dont use Annotated, because if you use Annotated, 
# the order of the parameters doesn't matter,
# we can do:

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# NOTES
# In standard Python, once you provide a default value for a parameter (using =), 
every parameter that follows it must also have a default value.

# This is a SYNTAX ERROR in Python
# def calculate(tax=0.05, price): 
#     return price + (price * tax)

# Python doesn't allow this because if you called calculate(100), 
# it wouldn't know if 100 is the tax or the price
# This is why Annotated is so useful, because it allows you to declare parameters without default values,