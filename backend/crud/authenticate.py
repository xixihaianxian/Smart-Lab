from sqlalchemy import update,select,text,and_
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import auth
from entity.user import Users
from typing import Union,Any
from utils import tools

async def login_auth(response:auth.LoginRequest,database:AsyncSession):
    # 获取登录时的用户姓名或者密码
    password=response.password
    email=response.email
    # 查询
    stmt=select(
        Users
    ).where(
        Users.email==email
    )
    result=await database.execute(
        statement=stmt
    )
    user_info=result.scalar_one_or_none()
    # 用户没有注册
    if user_info is None:
        return user_info
    else:
        # 验证密码是否正确
        hashed_password=user_info.password
        result=tools.verify_password(hashed_password=hashed_password,password=password)
        # 密码正确返回用户数据
        if result:
            return user_info
        # 密码错误返回None
        else:
            return None