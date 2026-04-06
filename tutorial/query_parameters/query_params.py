from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): # query parameters are defaulted
    return fake_items_db[skip : skip + limit]

# When you declare other function parameters that are not part of the path parameters, 
# they are automatically interpreted as "query" parameters.

# The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.]
# EX URL: http://127.0.0.1:8000/items/?skip=0&limit=10
# The query parameters are skip=0 and limit=10, and they are naturally 
# interpreted as strings, but FastAPI will convert them to the declared types (int in this case) and validate them.

# Going to http://127.0.0.1:8000/items/?skip=20 will change a default value.