from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, TestBForm, TestAForm, TestCForm, TestC1Form
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm, TestBForm, TestAForm, TestCForm, CompareForm
from .TestB import questions
from .TestA import questionsA
from .TestC import questionsC
from .models import TestB, TestA, TestC
from django.conf import settings
import os
import numpy as np


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
    found, data, labels, o, c, e, a, n = False, [0, 0, 0, 0, 0], [], None, None, None, None, None 
    scoreA = TestA.objects.filter(user__exact = request.user)
    scoreB = TestB.objects.filter(user__exact = request.user)
    scoreC = TestC.objects.filter(user__exact = request.user)
    if scoreA and scoreB and scoreC:
        for sA, sB, sC in zip(scoreA, scoreB, scoreC):
            data[0] = int(np.round((sA.o + sB.o + sC.o)/3, 0))
            data[1] = int(np.round((sA.c + sB.c + sC.c)/3, 0))
            data[2] = int(np.round((sA.e + sB.e + sC.e)/3, 0))
            data[3] = int(np.round((sA.a + sB.a + sC.a)/3, 0))
            data[4] = int(np.round((sA.n + sB.n + sC.n)/3, 0))
            labels = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
            o,c,e,a,n = [data[0], 100-data[0]], [data[1], 100-data[1]], [data[2], 100-data[2]], [data[3], 100-data[3]], [data[4], 100-data[4]]
        found = True
    context =  { 'labels': labels, 'data': data, 'user':user, 'found':found, 'o':o, 'c':c,'e':e, 'a':a, 'n':n}
    return render(request, 'scores.html',context)

@login_required
def profile(request):
    user = request.user.username
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Information updated successfully!')
            return redirect('tests')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user' : user, 'form' : form}
    return render(request, 'profile.html', context)

@login_required
def compare(request):
    user = request.user.username
    valid, found, get, data_user, data_compare, labels, user_attempt, compare_attempt = False, False, True, [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [], False, False
    if request.method == "POST":
        get = False
        form = CompareForm(request.POST)  
        if  form.is_valid():
            query =  form.cleaned_data['query']
            comparison = User.objects.filter(username__iexact=query[0:]).first()
            if comparison:  
                found = True
                scoreA_user = TestA.objects.filter(user__exact = request.user)
                scoreB_user = TestB.objects.filter(user__exact = request.user)
                scoreC_user = TestC.objects.filter(user__exact = request.user)
                scoreA_compare = TestA.objects.filter(user__exact = comparison)
                scoreB_compare = TestB.objects.filter(user__exact = comparison)
                scoreC_compare = TestC.objects.filter(user__exact = comparison)
                if scoreA_user and scoreB_user and scoreC_user:
                    for sA, sB, sC in zip(scoreA_user, scoreB_user, scoreC_user):
                        data_user[0] = int(np.round((sA.o + sB.o + sC.o)/3, 0))
                        data_user[1] = int(np.round((sA.c + sB.c + sC.c)/3, 0))
                        data_user[2] = int(np.round((sA.e + sB.e + sC.e)/3, 0))
                        data_user[3] = int(np.round((sA.a + sB.a + sC.a)/3, 0))
                        data_user[4] = int(np.round((sA.n + sB.n + sC.n)/3, 0))
                        user_attempt = True
                        labels = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
                if scoreA_compare and scoreB_compare and scoreC_compare:
                    for sA, sB, sC in zip(scoreA_compare, scoreB_compare, scoreC_compare):
                        data_compare[0] = int(np.round((sA.o + sB.o + sC.o)/3, 0))
                        data_compare[1] = int(np.round((sA.c + sB.c + sC.c)/3, 0))
                        data_compare[2] = int(np.round((sA.e + sB.e + sC.e)/3, 0))
                        data_compare[3] = int(np.round((sA.a + sB.a + sC.a)/3, 0))
                        data_compare[4] = int(np.round((sA.n + sB.n + sC.n)/3, 0))
                        compare_attempt = True
                return render(request, 'compare.html', {'user':user, 'form':form, 'get':get, 'found':found, 'user_attempt':user_attempt, 'compare_attempt':compare_attempt, 'data_user': data_user, 'data_compare': data_compare, 'labels':labels, 'comparison':comparison})                             
            else:
                return render(request, 'compare.html', {'user':user, 'form':form, 'get':get, 'found':found})

    else:
        form = CompareForm()
        return render(request, 'compare.html', {'user':user, 'form':form, 'get':get})

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
            ocean,status,flag = form.process()
            if status:
                if flag == "fill":
                    print(ocean)
                    instance = TestC(user = request.user, o = ocean[0], c = ocean[1], e = ocean[2], a = ocean[3], n = ocean[4])
                    instance.save()
                    messages.success(request, f'Your response for test C has been saved.')
                    return redirect('tests')
                else:
                    messages.success(request, f'No posts found, please attempt the alternate test.')
                    return redirect('testC')
            else:
                messages.error(request, f'Invalid credentials, please check your reponse.')
                return redirect('testC')
    else:
        form = TestCForm()
    context = {'user' : user, 'form' : form}
    return render(request, 'TestC.html', context)
        
@login_required
def testC1(request):
    user = request.user.username
    q = list(questionsC.get_values_for_questions())
    if request.method == 'POST':
        form = TestC1Form(request.POST)
        if  form.is_valid():
            ocean = form.process()
            instance = TestC(user = request.user, o = ocean[0], c = ocean[1], e = ocean[2], a = ocean[3], n = ocean[4])
            instance.save()
            messages.success(request, f'Your response for test C has been saved.')
            return redirect('tests')
    else:
        form = TestC1Form()
    context = {'user' : user, 'form' : form, 'q': q}
    return render(request, 'TestC1.html', context)


@login_required
def logout_view(request):
    logout(request)
    messages.info(request,'You have been logged out.')
    return redirect('home')