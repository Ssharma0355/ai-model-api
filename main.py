from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open('patient.json','r') as f:
       data = json.load(f)

    return data

@app.get("/")
def home():
    return {"message":"This is my 1st fastapi"}

@app.get("/about")
def about():
    return {"message":"This is about page"}

@app.get("/showData")
def showData():
    return load_data()