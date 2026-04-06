# When we don't need to declare more validations or metadata, 
# we can make the q query parameter required just by not declaring a default value, like:
# q: str

# instead of:

# q: str | None = None

# But we are now declaring it with Query, for example like:

# q: Annotated[str | None, Query(min_length=3)] = None

# So, when you need to declare a value as required while using Query, 
# you can simply not declare a default value

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# You can also declare that a parameter accept None, but that it's still required.
# This would force clients to send a value, even if the value is None. 

# To do that, you can declare that None is a valid type but simply do not declare a default value, like:
# q: Annotated[str | None, Query(min_length=3)]