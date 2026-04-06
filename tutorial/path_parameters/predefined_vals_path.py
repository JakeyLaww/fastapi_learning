from enum import Enum

from fastapi import FastAPI

# `Enum` is a class that allows you to create enumerations, which are a set of symbolic names (members) bound to unique, constant values.
# In this example we will use an Enum to define a set of fixed values for a path parameter.

# ModelName is an Enum class with three members: ModelName.alexnet, ModelName.resnet and ModelName.lenet.
# Each member’s value is the string on the right side: ModelName.alexnet.value == "alexnet"

class ModelName(str, Enum): 
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
# so every member is a string and also an Enum member. This allows FastAPI to know that the values must be of type string and will be able to render correctly in the API docs.

# ModelName is an an Enum class that defines three members: alexnet, resnet and lenet. 
# Only these all the allowed URLS
# http://127.0.0.1:8000/models/alexnet
# http://127.0.0.1:8000/models/resnet
# http://127.0.0.1:8000/models/lenet


app = FastAPI()

# model_name in the path becomes a ModelName value
# FastAPI converts the path segment into one of the enum members
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # Checks if value is "alexnet"
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": # Checks if value is "lenet". You can also check the value of the enum member with the .value attribute
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# Notes
# If you have a path operation that recieves a path parameter, but you want the possible valid path parameter values
# to be predefined, you can use an Enum class to define the possible values.

# Import Enum and create a sub-class that inherits from str and from Enum.
# By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.
# Then create class attributes with fixed values, which will be the available valid values