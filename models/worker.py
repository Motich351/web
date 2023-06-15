from typing import List
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from database import Worker


WorkerOut = sqlalchemy_to_pydantic(Worker)


class WorkerIn(sqlalchemy_to_pydantic(Worker)):
    class Config:
        orm_mode = True


class WorkersOut(BaseModel):
    workers: List[WorkerOut]