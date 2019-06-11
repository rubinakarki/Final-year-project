from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name ='home'),
    path('camera/',views.camera,name = 'camera'),
    path('register/',views.register,name ='register'),
    path('logout/',views.logout_request,name ='logout'),
    path('login/',views.login_request,name ='login'),
]
