from fastapi import APIRouter,Depends,status
from fastapi import HTTPException
from schemas import auth
from utils import database_connection,tools
from sqlalchemy.ext.asyncio import AsyncSession
from crud import authenticate

router =APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)

@router.post(path="/login")
async def login(response:auth.LoginRequest,database:AsyncSession=Depends(database_connection.get_db)):
    user=await authenticate.login_auth(response=response,database=database)
    # 验证失败
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect email or password")
    # 登录成功
    else:
        login_response=auth.LoginResponse.model_validate(user)
        return tools.serialization_response(
            status=status.HTTP_200_OK,
            message="success",
            data=login_response
        )