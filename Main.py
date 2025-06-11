from typing import Union 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Langchainlogic import create_restaurant
from Models import Restaurant, SessionLocal, init_db
from sqlalchemy.orm import Session


app = FastAPI()
init_db()  # Create DB and tables on app startup

#if my frontend (html, js) runs on a different domain than my backend (FastAPI), browser sees these 
#as different origins. so to prevent browser from blocking frontend to call backend, we have to do the below
app.add_middleware(
    CORSMiddleware, #adds CORS middleware to FastAPI app. Cross-origin resource sharing 
    allow_origins=["*"], #allows requests from any website/origin 
    allow_methods=["*"], #allows all HTTP methods (GET,POST,PUT,DELETE)
    allow_headers=["*"]  #allow all headers in the requests like authorization tokens, content-type etc
)

@app.get('/')
def read__root():
    return {"Hey! Are you looking to start a new restaurant? Don't know what type of cuisine? We got you covered"}

class GetCuisine(BaseModel): #reads JSON string and used GetCuisine(BaseModel) to turn it into a python object
    cuisine: str #expecting a json object with a string field called cuisine
    
@app.post('/restaurant')
#when someone sends a post request this function will be called
def get__menu(data: GetCuisine):
    
    result = create_restaurant(data.cuisine)
    db: Session = SessionLocal()
    try:
        restaurant = Restaurant(cuisine=data.cuisine,name=result['name'],menu_items=result['menu_items'])
        db.add(restaurant)
        db.commit()
        db.refresh(restaurant)
        return result 
    
    finally:
        db.close()
        
@app.get('/history')
def get_data():
    db: Session = SessionLocal()
    
    try:
        entries = db.query(Restaurant).all()
        return[
            {
                "id":entry.id,
                "cuisine":entry.cuisine,
                "name":entry.name,
                "menu_items":entry.menu_items
                
            }
            for entry in entries
        ]
    finally:
        db.close()

        
    
        
