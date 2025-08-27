from pydantic import BaseModel
from datetime import datetime

class NoteSchema(BaseModel):
    title: str
    content: str

class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.created_at = datetime.now()
