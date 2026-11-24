from fastapi import APIRouter,Depends
from schemas import auth
from utils import database_connection
from sqlalchemy.ext.asyncio import AsyncSession

router =APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)

@router.post(path="/login")
def login(response:auth.LoginRequest,database:AsyncSession=Depends(database_connection.get_db)):
    pass