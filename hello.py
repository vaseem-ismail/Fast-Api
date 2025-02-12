from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return("Hello this the Sample Content")

@app.get("/sample/{age}")
def findage(age: int):
    return("This is your Given Age, Age::{age}")

@app.get("/find/{:id}")
class User(BaseModel):
    name : str
    age : int
    email : EmailStr
    Password : str


if __name__ == "__main__":
    uvicorn.run("hello:app",port=3000,host="127.0.0.1")
