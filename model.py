# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SignUp(Base):
    __tablename__ = 'Sign_up'

    id = Column(INTEGER(11), primary_key=True)
    Name = Column(String(225), comment='Name of the user')
    Phone = Column(String(225), comment='User phone number ')
    Email = Column(String(225), comment='User’s Email')
    Password = Column(String(90), comment='User password')
    Type = Column(String(45), comment='Type of the user (user)')
    Status = Column(String(45), comment='Active or inactive')
