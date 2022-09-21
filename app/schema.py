from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    created: datetime
    class Config:
        orm_model = True

class PostCreate(PostBase):
    pass