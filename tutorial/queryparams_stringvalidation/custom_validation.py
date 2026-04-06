# There could be cases where you need to do some custom validation 
# that can't be done with the parameters shown above.

# In those cases, you can use a custom validator function that is applied 
# after the normal validation (e.g. after validating that the value is a str).

# You can achieve that using Pydantic's AfterValidator inside of Annotated. Pydantic has an BeforeValidator as well, but it is not supported in FastAPI at the moment.

# For example, this custom validator checks that the item ID starts with 
# isbn- for an ISBN book number or with imdb- for an IMDB movie URL ID:
import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

# This is the custom validation function that will be applied after the normal validation of the query parameter.
# value.startswith() can take a tuple of prefixes to check for, so we can check for both "isbn-" and "imdb-" at the same time.
def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    # AfterValidator() is a Pydantic validator that is applied after the normal validation of the query parameter
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        # list(data.items()) returns list of tuples (id, item) for each value in dictionary
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}

# EX GET request:
# GET /items/?id=isbn-9781529046137
# returns:
# {
#   "id": "isbn-9781529046137",
#   "name": "The Hitchhiker's Guide to the Galaxy"
# }

# EX of valid URL's:
# GET /items/
# GET /items/?id=isbn-9781529046137
# GET /items/?id=imdb-tt0371724
# GET /items/?id=isbn-9781439512982

# EX of invalid URL's:
# GET /items/?id=isbn
# GET /items/?id=foo-imbd-tt0371724