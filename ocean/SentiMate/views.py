from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, TestBForm
from .TestB import questions
from .models import TestB


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')	
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html', {'form':form})

@login_required
def tests(request):
    user = request.user.username
    return render(request, 'tests.html', {'user':user})

@login_required
def profile(request):
    user = request.user.username
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Information updated successfully!')
            return redirect('tests')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user' : user, 'form' : form}
    return render(request, 'profile.html', context)

@login_required
def testB(request):
    user = request.user.username
    q = list(questions.get_values_for_questions())
    if request.method == 'POST':
        form = TestBForm(request.POST)
        data = []
        if  form.is_valid():
            ocean = form.process()
            instance = TestB(user = request.user, o = ocean[0], c = ocean[1], e = ocean[2], a = ocean[3], n = ocean[4])
            instance.save()
            messages.success(request, f'Your response for test B has been saved.')
            return redirect('tests')
    else:
        form = TestBForm()
    context = {'user' : user, 'form' : form, 'q': q}
    return render(request, 'TestB.html', context)
        

@login_required
def logout_view(request):
    logout(request)
    messages.info(request,'You have been logged out.')
    return redirect('home')