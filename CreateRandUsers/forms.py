from django.forms import ModelForm, TextInput

from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['text']

        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'От 1 до 10',
            })
        }
