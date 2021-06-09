from django.forms import EmailInput, ModelForm, TextInput

from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
        }
