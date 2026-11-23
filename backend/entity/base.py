from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
from sqlalchemy import DATETIME,DateTime
from datetime import datetime

# 表基类
class BaseModel(DeclarativeBase):
    pass

# 时间基类
class TimeModel:
    created_at:Mapped[datetime]=mapped_column(
        DateTime,
        default=datetime.now,
    )
    updated_at:Mapped[datetime]=mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )