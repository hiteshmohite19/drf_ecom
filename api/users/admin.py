from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


# class UserAdmin(UserAdmin):
# class Meta:
# list_display = ("email", "mobile_no")


admin.site.register(User)
admin.site.register(UserAddress)
