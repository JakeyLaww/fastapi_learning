from fastapi import FastAPI

app = FastAPI()

# PATH PARAMETERS
# Path parameters are used to capture values from the URL path. 
# They are defined in the path string of the route and are passed as arguments to the path operation function.

# Path parameters are included directly in the URL path, seperated by a /. 
# For example, in the path /items/{item_id}, item_id is a path parameter.
# When a request is made to this path, the value of item_id will be extracted from the URL and passed to the function as an argument.
@app.get("/items/{item_id}")
async def read_item(item_id : int): # Note that the type of item_id is declared as int. FastAPI will convert it to int and validate it.
    return {"item_id": item_id}

# You can declare path "parameters" or "variables" with the same syntax used by Python format strings
# The value of the path parameter item_id will be passed to your function as the argument item_id.
# http://127.0.0.1:8000/items/5 will return {"item_id": 5}