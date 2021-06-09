from django import forms
from .models import Person
from django.forms import ModelForm, TextInput, EmailInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
        }