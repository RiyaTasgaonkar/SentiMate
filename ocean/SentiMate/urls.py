from django.urls import path,include
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('ocean',views.ocean, name='ocean'),
    path('register',views.register, name='register'),
    path('login',authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('tests',views.tests, name='tests'),
    path('scores',views.scores, name='scores'),
    path('profile',views.profile, name='profile'),
    path('testB',views.testB, name='testB'),
    path('testA',views.testA, name='testA'),
    path('testC',views.testC, name='testC'),
]