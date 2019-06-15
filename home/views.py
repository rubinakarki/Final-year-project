from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import base64
import os
import re
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from datetime import time
import numpy as np
from model.recognize import recognize
from home.models import Songs
from django.conf import settings
# Create your views here.

def home(request):
    return render(request,'home.html')

def playlist(request):
    list_of_songs  =  Songs.objects.all().order_by('name')
    return render(request,'playlist.html',{'list': list_of_songs}) 
    
@login_required(login_url= settings.LOGIN_URL)
def chatroom(request):
   return render(request,'chatroom.html')

@login_required(login_url= settings.LOGIN_URL)
def camera(request):
    return render(request,'camera.html')

@csrf_exempt
def predict(request):
    img_data = request.POST.get("images")
   
    format, imgstr = img_data.split(';base64,') 
    ext = format.split('/')[-1] 

    data = ContentFile(base64.b64decode(imgstr), name='pictures/output.png')

    #  Saving POST'ed file to storage
    # file =request.FILES['myfile']
   
    file_name = default_storage.save("pictures/output.png", data)

    result = recognize(file_name)
    label = ['angry','disgust','fear','happy','neutral','sad','surprise']    
    return HttpResponse(label[result[0]])  
    

def recommend(request,emotion):
    if emotion =='angry':
        songs =  Songs.objects.filter(angry__gt = 0.5).order_by('name')
    elif emotion =='disgust':
        songs =  Songs.objects.filter(disgust__gt = 0.5 ).order_by('name')
    elif emotion =='fear':
        songs  =  Songs.objects.filter(fear__gt = 0.5).order_by('name')
    elif emotion=='happy':
        songs  =  Songs.objects.filter(happy__gt = 0.5).order_by('name')
    elif emotion =='neutral':
        songs =  Songs.objects.filter(neutral__gt = 0.5).order_by('name')
    elif emotion =='sad':
        songs =  Songs.objects.filter(sad__gt = 0.5).order_by('name')
    elif emotion =='surprise':
        songs  =  Songs.objects.filter(surprise__gt = 0.5).order_by('name')
    # import ipdb; ipdb.set_trace()
    return render(request,'recommendsong.html',{'emotion' : emotion,'songs' : songs})
    
def register(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New account created as  {username}")
            login(request,user) 
            messages.info(request,f"You are now logged in as {username}")
            return redirect('/')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect("/")

def login_request(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None :
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
            
         
    form = AuthenticationForm()
    return render(request,'login.html',{'form': form})
