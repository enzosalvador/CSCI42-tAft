from django.forms import ModelForm
from .models import *
from django import forms

class FoodForm(ModelForm):
    class Meta:
        model = FoodModel
        fields = "__all__"

        labels = {
            'food_id': '',
            'food_name': '',
            'calories_per_serving': '',
            'carbs_per_serving': '',
            'protein_per_serving': '',
            'fat_per_serving': '',
        }

        widgets = {
            'food_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Food ID'}),
            'food_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
            'calories_per_serving': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calories per Serving'}),
            'carbs_per_serving': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Carbohydrates per Serving'}),
            'protein_per_serving': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Proteins per Serving'}),
            'fat_per_serving': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fats per Serving'}),
        }