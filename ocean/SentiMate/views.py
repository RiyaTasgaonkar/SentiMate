from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, TestBForm, TestAForm, TestCForm
from .TestB import questions
from .TestA import questionsA
from .models import TestB, TestA, TestC


# Create your views here.
def home(request):
    return render(request,'home.html')

def ocean(request):
    return render(request,'ocean.html')

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
def scores(request):
    user = request.user.username
    found, data, labels = False, [], []
    score = TestB.objects.filter(user__exact = request.user)
    if score:
        for s in score:
            data = [s.o, s.c, s.e, s.a, s.n]
            labels = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
        found = True
    context =  { 'labels': labels, 'data': data, 'user':user, 'found':found }
    return render(request, 'scores.html',context)

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
def tests(request):
    user = request.user.username
    return render(request, 'tests.html', {'user':user})

@login_required
def testA(request):
    user = request.user.username
    q = list(questionsA.get_questions_and_options())
    if request.method == 'POST':
        form = TestAForm(request.POST)
        if  form.is_valid():
            ocean = form.process()
            instance = TestA(user = request.user, o = ocean[0], c = ocean[1], e = ocean[2], a = ocean[3], n = ocean[4])
            instance.save()
            messages.success(request, f'Your response for test A has been saved.')
            return redirect('tests')
    else:
        form = TestAForm()
    context = {'user' : user, 'form' : form, 'q': q}
    return render(request, 'TestA.html', context)

@login_required
def testB(request):
    user = request.user.username
    q = list(questions.get_values_for_questions())
    if request.method == 'POST':
        form = TestBForm(request.POST)
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
def testC(request):
    user = request.user.username
    if request.method == 'POST':
        form = TestCForm(request.POST)
        if form.is_valid():
            ocean = form.process()
            print(ocean)
            instance = TestC(user = request.user, o = ocean[0], c = ocean[1], e = ocean[2], a = ocean[3], n = ocean[4])
            instance.save()
            messages.success(request, f'Your response for test C has been saved.')
            return redirect('tests')
    else:
        form = TestCForm()
    context = {'user' : user, 'form' : form}
    return render(request, 'TestC.html', context)
        

@login_required
def logout_view(request):
    logout(request)
    messages.info(request,'You have been logged out.')
    return redirect('home')