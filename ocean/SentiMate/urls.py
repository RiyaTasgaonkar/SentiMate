from django.urls import path,include
from django.contrib.auth import views as authViews
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name='home'),
    path('ocean',views.ocean, name='ocean'),
    path('register',views.register, name='register'),
    path('login',authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('tests',views.tests, name='tests'),
    path('scores',views.scores, name='scores'),
    path('compare',views.compare, name='compare'),
    path('profile',views.profile, name='profile'),
    path('testB',views.testB, name='testB'),
    path('testA',views.testA, name='testA'),
    path('testC',views.testC, name='testC'),
    path('testC1',views.testC1, name='testC1')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
