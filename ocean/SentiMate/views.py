from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!')
            return redirect('login')
        else:
            messages.info(request,'Account creation be failed :(')
    else:
        form=UserCreationForm()
    return render(request,'register.html', {'form':form})

@login_required
def tests(request):
    user=request.user.username
    return render(request, 'tests.html', {'user':user})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request,'You have been logged out.')
    return redirect('home')