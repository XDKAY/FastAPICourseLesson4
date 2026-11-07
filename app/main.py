from fastapi import FastAPI
from .models import User


app = FastAPI()


@app.get("/")
async def root():
    return {"mesage": "Hello World!"}


@app.get("/users", response_model=User)
async def get_user():
    return User(
        id=1,
        name="John Doe",
    )
