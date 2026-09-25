from fastapi import FastAPI,HTTPException,status,Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel,EmailStr
from database import get_db
from model import User

app = FastAPI()

class UserInformation(BaseModel):
    name:str
    email:EmailStr
    
@app.get("/")
async def hello():
    return {
        'message':'Docker FastAPI is Running Successfully'
    }
    
@app.post("/insert")
async def add(user:UserInformation,db:Session=Depends(get_db)):
    new_user = User(
        name=user.name,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    
    return {
        "message":f"{user.name} Successfully added to database"
    }