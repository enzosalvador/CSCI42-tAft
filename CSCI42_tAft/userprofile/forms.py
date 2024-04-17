from django.forms import ModelForm
from .models import *
from django import forms

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfileModel
        fields = "__all__"

        labels = {
            'first name': '',
            'last name': '',
            'email': '',
            'height': '',
            'weight': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Height'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight'}),
        }