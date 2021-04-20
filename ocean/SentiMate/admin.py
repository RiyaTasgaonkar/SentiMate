from django.contrib import admin
from .models import Profile, TestB, TestA, TestC, TestC1

# Register your models here.
admin.site.register(Profile)
admin.site.register(TestA)
admin.site.register(TestB)
admin.site.register(TestC)
admin.site.register(TestC1)
