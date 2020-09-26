from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
    url(r'^register',views.saveRegister,name='register'),
    url(r'^login',views.authenticate_user,name='login'),

    

]