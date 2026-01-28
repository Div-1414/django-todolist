from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo.models import todo
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login


@login_required (login_url='login')
def home(request):
    undone_task=todo.objects.filter(user=request.user,is_completed=False).order_by('-created_at')
    done_task=todo.objects.filter(user=request.user,is_completed=True)
    context={
        'undone_task':undone_task,
        'done_task':done_task
    }
    return render(request,'home.html',context)

#view for register new user:-
from django.contrib.auth import login

def regiteruser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            users = form.save()
           
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'regiteruser.html', {'form': form})


def login(request):
    if request.method=='POST':
        loginuser=AuthenticationForm(request,request.POST)
        if loginuser.is_valid():
            user=loginuser.cleaned_data['username']
            password=loginuser.cleaned_data['password']

            user=auth.authenticate(username=user,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')    

    form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'login.html',context)

#function for logout:-
def logout(request):
    auth.logout(request)
    return redirect('login')