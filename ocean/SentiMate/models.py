from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    Male = 'M'
    Female = 'F'
    RatherNotSay = 'O'
    GENDER_CHOICES = ((Male, 'Male'),(Female, 'Female'),(RatherNotSay,'Rather Not Say'),)

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    emailid = models.EmailField(blank=False)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    gender = models.CharField(max_length = 20, choices = GENDER_CHOICES, default = Male)
    bio = models.TextField(max_length=250, blank=False)
    # image = models.ImageField(default = 'default.jpg' , upload_to = "profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class TestA(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    o = models.IntegerField(blank=False)
    c = models.IntegerField(blank=False)
    e = models.IntegerField(blank=False)
    a = models.IntegerField(blank=False)
    n = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.user.username} TestA'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class TestB(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    o = models.IntegerField(blank=False)
    c = models.IntegerField(blank=False)
    e = models.IntegerField(blank=False)
    a = models.IntegerField(blank=False)
    n = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.user.username} TestB'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
