from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str

class PostSchema(BaseModel):
    title: str
    content: str
    author_id: int

class CommentSchema(BaseModel):
    content: str
    post_id: int
    user_id: int
