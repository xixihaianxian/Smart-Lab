import yaml
import load_logger
from typing import Union
import os

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