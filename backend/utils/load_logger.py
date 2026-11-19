from loguru import logger
from pathlib import Path
import sys
import os
from dotenv import load_dotenv
from typing import Optional
from datetime import datetime

# 登录env
load_dotenv(Path(__file__).parent.parent / ".env")

logger_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
"<level>{level: <8}</level> | "
"<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
"<level>{message}</level>"

def logger_bar(log_file:Optional[str]=None):
    logger.remove()
    # 控制台日志配置
    logger.add(
        sink=sys.stderr,
        colorize=True,
        level=os.environ["LEVEL"],
        format=logger_format,
        serialize=True,
        backtrace=True,
        diagnose=True,
        enqueue=True
    )
    # 文件日志配置
    if log_file is None:
        now_time=datetime.now()
        now_time_str=now_time.strftime("%Y_%m_%d")
        log_dir=Path(__file__).parent.parent.joinpath("logs")
        # 日志目录不存在
        if not log_dir.exists():
            log_dir.mkdir(parents=True,exist_ok=True)
        log_file_name=f"{now_time_str}.log"
        log_file=log_dir.joinpath(log_file_name)
    logger.add(
    )