from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

User = os.getenv('user')
Port = os.getenv('port')
Password = os.getenv('password')
Host = os.getenv('host')
DBName = os.getenv('db')

DataBase_URL = f"postgresql+psycopg2://{User}:{Password}@{Host}:{Port}/{DBName}"
engine = create_engine(DataBase_URL)
Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()