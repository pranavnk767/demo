from django.db import models

# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy import CheckConstraint, Column, DateTime, Float, ForeignKey, Index, String, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGTEXT, SMALLINT, TINYINT, TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from django.contrib.auth.hashers import make_password, check_password


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

    def check_password(self, raw_password):
        return check_password(raw_password, self.Password)


