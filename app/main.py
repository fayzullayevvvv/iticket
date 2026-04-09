from fastapi import FastAPI

from app.db.session import engine
from app.models.base import Base
from app.models.user import User


app = FastAPI(title="Iticket API")
Base.metadata.create_all(engine)


@app.get("/")
async def root_view():
    return {"message": "project is running..."}
