from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models
from app.database import engine, get_db
from app.config import settings

print(settings.database_name)

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/sqlalchemy")
def read_users(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return {"successful":posts}