from sqlalchemy import update,select,text,and_
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import auth
from entity.user import Users

async def login_auth(response:auth.LoginRequest,database:AsyncSession):
    # 获取登录时的用户姓名或者密码
    password=response.password
    email=response.email
    # 查询
    stmt=select(
        Users
    ).where(
        and_(
            Users.username==email,
            Users.password==password
        )
    )
    result=await database.execute(
        statement=stmt
    )
    user_info=result.scalars()