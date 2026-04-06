# FastAPI is a Python class that provides all the functionality for your API.
from fastapi import FastAPI

# Here the app variable will be an "instance" of the class FastAPI.
# This will be the main point of interaction to create all your API.
app = FastAPI()

# Created a Path Operation
# "Path" here refers to the last part of the URL starting from the first /.
# A "path" is also commonly called an "endpoint" or a "route".
# "Operation" here refers to one of the HTTP "methods" (GET, POST, PUT, DELETE, etc).

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:
# the path /
# using a get operation
@app.get("/")
async def root():
    return {"message": "Hello World"}

# It will be called by FastAPI whenever it receives a request to the URL "/" using a GET operation.