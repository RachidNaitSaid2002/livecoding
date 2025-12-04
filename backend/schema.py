from pydantic import BaseModel



class UserLogin(BaseModel):
    email:str
    password:str

class UserRequest(UserLogin):
    name:str

class UserResponse(UserRequest):
    id:int

