from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from dotenv import load_dotenv
import os
from pathlib import Path
import load_logger
import tools

# load env
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

# load config
yaml_path=Path(__file__).parent.parent.joinpath("config","config.yaml")
tools.load_yaml(path=yaml_path)

# 获取配置
url=os.environ["DATABASE_URL"]
pool_size=int(os.environ["POOL_SIZE"])
echo=os.environ["ECHO"].lower()=="true"
max_overflow=int(os.environ["MAX_OVERFLOW"])
pool_recycle=int(os.environ["POOL_RECYCLE"])

engine=create_async_engine(
    url=url,
    pool_size=pool_size,
    max_overflow=max_overflow,
    pool_recycle=pool_recycle,
    echo=echo # 输出sql日志，测试时使用
)

session_maker=sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with session_maker() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()