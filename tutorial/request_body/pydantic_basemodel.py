from fastapi import FastAPI

# you need to import BaseModel from pydantic
from pydantic import BaseModel

# CREATE YOUR DATA MODEL 
# Then you declare your data model as a class that inherits from BaseModel.
# Use standard Python types for all the attributes
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# The same as when declaring query parameters, when a model attribute has a default value, 
# it is not required. Otherwise, it is required. Use None to make it just optional.

# For example, this model above declares a JSON "object" (or Python dict) like:
# {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
#     "tax": 3.5
# } # Note we can also omit the "description" and "tax" fields, as they are optional.

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): # add the model to the path operation function as a parameter
    return item
# Declared the same as we declared path and query parameters, but instead of a simple type, we use the model class as the type.
# Results:
# With just that Python type declaration, FastAPI will:

# Read the body of the request as JSON.
# Convert the corresponding types (if needed).
# Validate the data.
# If the data is invalid, it will return a nice and clear error, indicating exactly where and what was the incorrect data.
# Give you the received data in the parameter item.
# As you declared it in the function to be of type Item, you will also have all the editor support (completion, etc) for all of the attributes and their types.
# Generate JSON Schema definitions for your model, you can also use them anywhere else you like if it makes sense for your project.
# Those schemas will be part of the generated OpenAPI schema, and used by the automatic documentation UIs.

# EX:
# we run curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" ... our JSON body here
# The server will return the same JSON data if valid, or an error if invalid. You can also test it in the interactive API docs, which will also show you the expected JSON schema for the body.