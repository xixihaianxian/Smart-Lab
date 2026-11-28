import yaml
import jwt
import os
from . import load_logger
import bcrypt
from typing import Union,Dict,Any
from pydantic import BaseModel
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv

load_dotenv()

# 获取配置
expire_hours=int(os.environ["JWT_EXPIRE_HOURS"])
jwt_secret_key=os.environ["JWT_SECRET_KEY"]
jwt_algorithm=os.environ["JWT_ALGORITHM"]

# 获取日志
logger=load_logger.logger_bar()

# 登录yaml配置文件
def load_yaml(path:Union[str,os.PathLike[str]]):
    """
    Params:
        path: yaml文件的路径
    Returns:
        配置
    """
    try:
        with open(path,"r",encoding="utf-8") as f:
            file=yaml.safe_load(
                stream=f
            )
        logger.info(f"{path} read success!")
        return file
    except FileNotFoundError:
        logger.error(f"{path} not found!")
        raise FileNotFoundError(f"{path} not found!") from None

# 结构化response
def serialization_response(status:int,message:str,data:Union[Dict,BaseModel]):
    if hasattr(data,"model_dump"):
        data=data.model_dump(by_alias=True)
    return {
        "status":status,
        "message":message,
        "data":data
    }

# 创建jwt token
def create_access_token(user_id:int)->str:
    """
    创建JWT token
    Args:
        user_id: 用户id
    Returns:
        jwt token
    """
    logger.debug(f"create access token {user_id}")
    expire=datetime.now(tz=timezone.utc)+timedelta(hours=expire_hours)
    # 将过期时间转化为时间戳
    expire=expire.timestamp()
    payload={
        "user_id":user_id,
        "expire":expire
    }
    jwt_token=jwt.encode(
        payload=payload,
        key=jwt_secret_key,
        algorithm=jwt_algorithm
    )
    return jwt_token

# 解析jwt token
def decode_access_token(token:str)->dict:
    """
    解析jwt token
    Args:
        token: jwt token
    """
    result=jwt.decode(
        jwt=token,
        key=jwt_secret_key,
        algorithms=jwt_algorithm
    )
    return result

# 密码加密
def hash_password(password:str):
    """
    密码加密
    Args:
        password: 密码
    """
    result=bcrypt.hashpw(
        password=password.encode("utf-8"),
        salt=bcrypt.gensalt()
    )
    result=result.decode("utf-8")
    return result

# 密码验证
def verify_password(password:str,hashed_password:str)->bool:
    result=bcrypt.checkpw(
        password=password.encode("utf-8"),
        hashed_password=hashed_password.encode("utf-8")
    )
    return result