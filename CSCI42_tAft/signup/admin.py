from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = UserModel

admin.site.register(UserModel, UserAdmin)
