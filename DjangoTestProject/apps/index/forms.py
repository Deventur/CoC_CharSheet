from django import forms


class UserForm(forms.Form):
    name = forms.CharField(min_length=3)
    age = forms.IntegerField(min_value=1, max_value=100)
