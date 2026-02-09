from tkinter import Image
from django.contrib import admin
from app.models import News,Category

# Register your models here.

admin.site.register(Category)
admin.site.register(News)