from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
db = {}
class Item(BaseModel):
    Name: str
    Age:int
    Breed: str
@app.post("/")
def get_data(item:Item):
    db[item.Name] = {item.Age , item.Breed}
    return {"Info": item}

@app.get("/")
def get_all_data():
    return db

@app.delete("/")
def delete_data(Name:str):
    del db[Name]
    return db

@app.put("/")
def update_data(item:Item):
    db[item.Name] = {item.Age , item.Breed}
    return db
