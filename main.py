from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"This is my 1st fastapi"}

@app.get("/about")
def about():
    return {"message":"This is about page"}