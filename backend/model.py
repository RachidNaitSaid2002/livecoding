from db import Base
from sqlalchemy import Column, String, Integer

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    name = Column(String, index=True)
    password = Column(String, index=True)
