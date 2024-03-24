from django.contrib import admin
from .models import *

class FoodAdmin(admin.ModelAdmin):
    model = FoodModel
    list_display = ("food_name",)

admin.site.register(FoodModel, FoodAdmin)
