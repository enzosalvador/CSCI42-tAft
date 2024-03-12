from django.contrib import admin
from .models import *

class FoodAdmin(admin.ModelAdmin):
    model = FoodModel

admin.site.register(FoodModel, FoodAdmin)
