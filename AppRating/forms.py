from django import forms
from AppRating.models import  User, App, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('userid', 'password')