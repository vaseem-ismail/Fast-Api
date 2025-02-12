from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/") #methods or enpoints
def index():
    return ({"message":"This is a Sample Data"})

@app.get("/sample/{name}")
def stringname(name:str):
    return ({f"Myself, {name}!. Nice to Meet you all!!"})

@app.get("/v1/article/{id}")
def article(id:str):
    print(id)
    return({"Sample":f"This is the sample data,and the id is {id}"})




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)