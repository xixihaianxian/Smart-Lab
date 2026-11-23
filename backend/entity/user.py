from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,String
import base

class Users(base.BaseModel,base.TimeModel):
    __tablename__ = "users"
    id:Mapped[int]=mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    username:Mapped[str]=mapped_column(
        String(50),
        nullable=False,
    )
    password:Mapped[str]=mapped_column(
        String(50),
        nullable=False
    )
    email:Mapped[str]=mapped_column(
        String(50),
        nullable=False,
        unique=True,
    )
    role:Mapped[str]=mapped_column(
        String(50),
    )
    phone:Mapped[str]=mapped_column(
        String(50),
        unique=True,
    )
    avatar:Mapped[str]=mapped_column(
        String(50),
    )
    status:Mapped[int]=mapped_column(
        String(1),
        default="1",
        comment="1:激活,0:禁用"
    )