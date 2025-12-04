from fastapi import FastAPI, Depends
from db import Base, Sessionlocal, engine
from model import Users
from schema import UserRequest, UserResponse, UserLogin
from jose import jwt
from dotenv import load_dotenv
import os
from fastapi.security import HTTPBearer, HTTPBasicCredentials

from fastapi.middleware.cors import CORSMiddleware



load_dotenv()

algorithm = os.getenv('algorithm')
secret_key = os.getenv('secret_key')

type_token = HTTPBearer()

Base.metadata.create_all(engine)
app = FastAPI()
db = Sessionlocal()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)


@app.get('/')
def root():
    return {'message':'Hello World !!'}


@app.post('/signup')
def signup(user:UserRequest):
    db_user = Users(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {'message':'User Created !!'}

@app.post('/login')
def login(user:UserLogin):
    db_user = db.query(Users).filter(user.email == Users.email).first()
    if db_user:
        email = db_user.email
        payload = {'sub':email}
        token = jwt.encode(payload, secret_key)
        return token
    else:
        return {'message' : 'User Not exist !!'}
    
@app.get('/Users')
def Get_User(token: HTTPBasicCredentials = Depends(type_token)):
    My_token = token.credentials
    payload = jwt.decode(My_token, secret_key)
    if payload:
        users = db.query(Users).all()
        return users
    else:
        return {'message':'You dont have access !!'}