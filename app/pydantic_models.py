from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
    
class UserToCreate(BaseModel):
    username: str
    password: str