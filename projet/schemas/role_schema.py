from pydantic import BaseModel


class RoleSchema(BaseModel):
    codrole: int  # PrimaryKey
    librole: str
    class Config:
        orm_mode = True