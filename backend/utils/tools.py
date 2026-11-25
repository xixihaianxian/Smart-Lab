import yaml
from . import load_logger
from typing import Union,Dict,Any
import os
from pydantic import BaseModel

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


def serialization_response(status:int,message:str,data:Union[Dict,BaseModel]):
    if hasattr(data,"model_dump"):
        data=data.model_dump(by_alias=True)
    return {
        "status":status,
        "message":message,
        "data":data
    }