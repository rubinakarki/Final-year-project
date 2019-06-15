from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name ='home'),
    path('playlist/',views.playlist,name = 'playlist'),
    path('chatroom/',views.chatroom,name = 'chatroom'),
    path('camera/',views.camera,name = 'camera'),
    path('register/',views.register,name ='register'),
    path('logout/',views.logout_request,name ='logout'),
    path('login/',views.login_request,name ='login'),
    path('predict/',views.predict,name ='predict'),
    path('recommend/<emotion>',views.recommend,name= 'recommend'),
]