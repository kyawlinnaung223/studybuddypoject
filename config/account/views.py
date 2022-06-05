from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import HttpResponse
from .models import Room,Topic,Messages
from .forms import RoomCreateForm


def homepageview(request):
    p=request.GET.get('p') if request.GET.get('p') != None else ''
   
    
    rooms=Room.objects.filter(
        Q(topic__name__contains=p)|
        Q(name__contains=p)|
        Q(description__contains=p)
       
        ).order_by('-Created')
    topics=Topic.objects.all()
    
    rooms_count=rooms.count()
    
    
    context={'rooms':rooms,'topics':topics,'rooms_count':rooms_count}
    
    return render(request,'home.html',context)


#this is navarpageview
def navarpageview(request):
    topics=Topic.objects.all()[:4]
    context={'topics':topics}
    return render(request,'navar.html',context)
#end navarpageview



# this is user profilepageivews
def userProfilepaveview(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    context={'user':user,'rooms':rooms}
    return render (request,'profile.html',context)
# end profilepageivews


#this is roompageview
def roompageview(request, pk):
    room=Room.objects.get(id=pk)
    messages=room.messages_set.all().order_by('-Created')
    participants=room.participants.all()
    if request.method == 'POST':
        message=Messages.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room_page',pk=room.id)
    context={'room':room,'messages':messages,'participants':participants}
   

    
  
    return render(request,'room.html',context)

#this is roomcreatepageview
@login_required(login_url='login')
def roomcreatepageview(request):
    form=RoomCreateForm()
    if request.method == 'POST':
        form=RoomCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form':form}
    return render(request,'create/room_create.html',context)
#end roomcreatepageview


#start roomupdatepageview
def roomUpdatepageview(request, pk):
    room=Room.objects.get(id=pk)
    form=RoomCreateForm(instance=room)
    if request.method == 'POST':
        form=RoomCreateForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'create/room_create.html',context)
#end roomupdatepageivew



#this is roomdeletepageview
def roomdeletepageview(request, pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context={'room':room}
        
    return render(request,'delete.html',context)
#end roomdeletepageview
    
  
#this is login views page
def loginpageivew(request):
    if request.method == 'POST':
        newusername=request.POST.get('username')
        newpassword=request.POST.get('password')
        try:
            user=User.objects.get(newusername=username,newpassword=password)
        except:
            messages.error(request,'User does not exists')
        user=authenticate(request,username=newusername,password=newpassword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password Inviald')
   
    return render(request,'login.html')
  
#end login views page

#this is register pageviews
def registerpageview(request):
    return render(request,'register.html')
#end registerpageviews



#this is delete messages
def messagesdeletepageview(request, pk):
    message=Messages.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context={'message':message}
        
    return render(request,'delete.html',context)

#end delete messages
