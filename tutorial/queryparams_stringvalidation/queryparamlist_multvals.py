# When you define a query parameter explicitly with Query you can also declare 
# it to receive a list of values, or said in another way, to receive multiple values.

# For example, to declare a query parameter q that can appear multiple times 
# in the URL.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
# This means q is a query parameter
# q is of type list[str] (FastAPI can collect multiple string values) or None (optional if not provided)
# Query() is just metadata telling FastAPI that this is a query parameter, and it can also be used to declare additional validations and metadata.
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

# Then, with a URL like:
# http://localhost:8000/items/?q=foo&q=bar
# you would receive the multiple q query parameters' values (foo and bar) 
# in a Python list inside your path operation function, in the function parameter q.

# So, the response to that URL would be:
# {
#   "q": [
#     "foo",
#     "bar"
#   ]
# }
# Note you may also used "q: Annotated[list, Query()] = []"
# to declare that q is a list of any type, and that it defaults to an empty list if not provided.