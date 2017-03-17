from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']