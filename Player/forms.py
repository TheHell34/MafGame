from django import forms

from .models import player

class RegisterForm(forms.ModelForm):
    class Meta:
        model = player
        fields = ('name', 'password',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = player
        fields = ('name', 'password',)