from django.contrib import admin
from .models import *

class ExerciseAdmin(admin.ModelAdmin):
    model = ExerciseModel

admin.site.register(ExerciseModel, ExerciseAdmin)
