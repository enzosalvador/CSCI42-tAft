from django.forms import ModelForm
from .models import *
from django import forms

class ExerciseForm(ModelForm):
    class Meta:
        model = ExerciseModel
        fields = "__all__"

        labels = {
            'exercise_id': '',
            'exercise_name': '',
            'calories_burned_per_hour': '',
        }

        widgets = {
            'exercise_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Exercise ID'}),
            'exercise_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exercise Name'}),
            'calories_burned_per_hour': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calories Burned per Hour'}),
        }