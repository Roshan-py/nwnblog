from django.shortcuts import render
from .models import Post , AllLogin
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm, SignUpForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.cache import cache

def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def dashboard(request):
    if request.user.is_authenticated:
        posts =Post.objects.all()
        user = request.user
        full_name =user.get_full_name()
        group = user.groups.all()
        ct= cache.get('count', version=user.pk)
        last = AllLogin.objects.create(user=request.user)
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'group':group,'ct':ct,'last':last})
    else:
        return HttpResponseRedirect('/login/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form= PostForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Your Post added sucessfully to Dashboard..!!!')
                form.save()
        else:
                form=PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! you have successfully signed up...!!!')
            user = form.save()
            group= Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form= SignUpForm()
    return render(request,'blog/signup.html',{'form':form})


def user_signout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            messages.warning(request,'user does not exist')
            form= LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname =form.cleaned_data['username']
                upass =form.cleaned_data['password']
                user= authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'logged in Successfully !!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/signin.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')
