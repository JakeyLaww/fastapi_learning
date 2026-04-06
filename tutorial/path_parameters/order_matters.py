from fastapi import FastAPI

app = FastAPI()

# Note that the path /users/me is defined before the path /users/{user_id}.
# This is because FastAPI will match the paths in the order they are defined.
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}