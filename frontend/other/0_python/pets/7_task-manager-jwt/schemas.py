from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    username: str
    role: str
    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    name: str

class ProjectResponse(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: str
    project_id: int
    owner_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    project_id: int
    owner_id: int
    class Config:
        orm_mode = True
