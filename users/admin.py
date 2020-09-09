from django.contrib import admin
from .models import customuser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','age','name')

admin.site.register(customuser,UserAdmin)