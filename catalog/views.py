from django.shortcuts import render
import jwt,json
import os
from dateutil.relativedelta import relativedelta
from datetime import datetime 
from datetime import datetime , date
from sqlalchemy import inspect, asc, desc, text, func, extract, and_
from sqlalchemy.orm import load_only
from sqlalchemy.exc import SQLAlchemyError
from rest_framework.response import Response
from rest_framework.views import APIView
from mysite import dbsession
from decimal import Decimal
from mysite.SqlAlcchemyencoder import AlchemyEncoder
import string,random
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes, renderer_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate, get_user, login
import pandas as pd
from catalog.models import SignUp
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from sqlalchemy import or_

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([AllowAny, ])
def saveRegister(request):
    try:
        session = dbsession.Session()

        Name = request.data['Name']
        Phone = request.data['Phone']
        Email = request.data['Email']
        Password = make_password(request.data['Password'])
        Type = request.data['Type']
        Status = 'A'
        
        
        email_check = session.query(SignUp).filter(SignUp.Email==Email).all()
        if(len(email_check) > 0):
            return Response({'status': 'email Id exists','message':'email Id already exists'})
        phno_check = session.query(SignUp).filter(SignUp.Phone==Phone).all()
        if(len(phno_check) > 0):
            return Response({'status': 'phone num exists','message':'phone num already exists'})

        user = SignUp()

        user.Name = Name
        user.Phone = Phone
        user.Email = Email
        user.Password = Password
        user.Type = Type
        user.Status = Status
        
        session.add(user)
        session.commit()
        session.close()
        return Response({'response': 'Data saved success fully'})
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
        session.close()
        return Response({'response': 'Error occured'})



@api_view(['GET','POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        session = dbsession.Session()

        Email = request.data['Email']
        Password =request.data['Password']
        user_id  = request.data['user_id']
        Phone  = request.data['Phone']
        
        
        user = session.query(SignUp).filter(or_(SignUp.Phone == Phone, SignUp.Email==Email,SignUp.id == user_id)).one()
        user_id = user.id
        if user.check_password(Password):
            user.Status = 'A'
            session.commit()
            columns =['Email','Phone','Name']
            user_list = session.query(SignUp.Email,SignUp.Phone,SignUp.Name).filter(or_(SignUp.Phone == Phone, SignUp.Email==Email,SignUp.id == user_id)).all()
            print(user_list)
            user_list = json.dumps(user_list, cls=AlchemyEncoder)
            user_list = pd.read_json(user_list)
            print(user_list.columns)
            if columns:
                user_list.columns = columns
                user_list = user_list.to_json(orient='records')
                return Response({'response': 'success','data':json.loads(user_list)})

        else:
            return Response({'response': 'Error','message':'Please provide a valid credentails'})

        return Response({'response': 'success'})
    except SQLAlchemyError as e:
        session.rollback()
        session.close()
        return Response({'response': 'Error occured'})





