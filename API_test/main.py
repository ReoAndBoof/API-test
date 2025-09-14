from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}

@app.get("/data")
def get_data():
    return {"data": [1, 2, 3]}
