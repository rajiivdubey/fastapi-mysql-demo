from fastapi import FastAPI, Depends
from database import get_db
from models import Employees
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Learning FastAPI"}

@app.get("/data")
def get_data(db: Session = Depends(get_db)):
    # Fetch all rows from 'users' table
    employees = db.query(Employees).all()

    # Convert ORM objects to dictionaries
    result = [
        {"id": user.id, "name": user.name, "salary": user.salary}
        for user in employees
    ]

    return result

