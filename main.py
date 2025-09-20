from fastapi import FastAPI, Path, HTTPException, Query
import json
app = FastAPI()

def load_data():
    with open('patient.json','r') as f:
       data = json.load(f)

    return data

def load_userData():
    with open('users.json','r') as f:
        users_data = json.load(f)
    return users_data
        
@app.get("/")
def home():
    return {"message":"This is my 1st fastapi"}

@app.get("/about")
def about():
    return {"message":"This is about page"}

@app.get("/showData")
def showData():
    return load_data()

@app.get("/users")
def get_users():
    return load_userData()
    # return load_userData()

@app.get("/users/{user_id}")
def users_details(user_id: str = Path(..., description="ID of the u1", example="u1")):
    data = load_userData()
    if user_id in data:
        return data[user_id]
        # return data[user_id]
    
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/patient/{patient_id}")
# Path can added for validations and message to the end point
def patient_detail(patient_id: str = Path(..., description="ID is P001 type", example="P001")):
    # 1st we will load the data 
    data = load_data()
    #then we check that if patient id is inside the load data or not
    if patient_id in data:
        #if data found the we will return with specific data id
        return data[patient_id]
    #if not found then we will give a error message
    # return {"message":"Patient not found"}
    
    # instead of message we will raise and change the status code and give the description 
    raise HTTPException(status_code=404, detail="Patient not found!")



@app.get("/sort")
def sort_patient(sort_by: str = Query(...,description="Sort patient by height and BMI"),order: str =Query('asc', description="sort in ascending and decending")):
    valid_feilds = ["height","weight","bmi"]
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400, detail="Invalid Feild {valid_feilds}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order")
    #loaded the data and filter 
    data = load_data()
    sort_order = True if order =="desc" else True

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order )
    return sorted_data