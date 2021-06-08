from django import forms


class TriangleForm(forms.Form):
    angle = forms.IntegerField(label='Angle X', max_value=360, min_value=1)
    angle2 = forms.IntegerField(label='Angle Y', max_value=360, min_value=1)
