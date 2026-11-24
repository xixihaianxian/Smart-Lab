from pydantic import BaseModel,Field,ConfigDict
from typing import Optional

class LoginRequest(BaseModel):
    # username:str=Field(
    #     validation_alias="userName",
    #     serialization_alias="userName",
    # )
    email:str=Field(
        validation_alias="email",
        serialization_alias="email"
    )
    password:str=Field(
        validation_alias="passWord",
        serialization_alias="passWord"
    )
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class RegisterRequest(BaseModel):
    username:str=Field(
        validation_alias="userName",
        serialization_alias="userName",
    )
    password:str=Field(
        validation_alias="passWord",
        serialization_alias="passWord"
    )
    email:str=Field(
        validation_alias="email",
        serialization_alias="email",
    )
    model_config=ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

class LoginResponse(BaseModel):
    id:int=Field(
        validation_alias="id",
        serialization_alias="id",
    )
    username:str=Field(
        validation_alias="userName",
        serialization_alias="userName",
    )
    role:str=Field(
        validation_alias="role",
        serialization_alias="role",
    )
    email:Optional[str]=Field(
        validation_alias="email",
        serialization_alias="email",
    )
    phone:Optional[str]=Field(
        validation_alias="phone",
        serialization_alias="phone",
        default=None
    )
    model_config = ConfigDict(
        from_attributes=True, # 允许使用对象来创建示例
        populate_by_name=True # 允许使用字段名或者别名进行输入
    )