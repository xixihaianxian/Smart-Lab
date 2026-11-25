from sqlalchemy import update,select,text,and_
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import auth
from entity.user import Users
from typing import Union,Any

async def login_auth(response:auth.LoginRequest,database:AsyncSession):
    # 获取登录时的用户姓名或者密码
    password=response.password
    email=response.email
    # 查询
    stmt=select(
        Users
    ).where(
        and_(
            Users.email==email,
            Users.password==password
        )
    )
    result=await database.execute(
        statement=stmt
    )
    user_info=result.scalar_one_or_none()
    # 返回user info
    return user_info