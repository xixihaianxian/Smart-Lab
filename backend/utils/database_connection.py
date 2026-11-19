from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from dotenv import load_dotenv
import os
from pathlib import Path

# load env
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

# load config


engine=create_async_engine(
)