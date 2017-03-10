from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    username = forms.CharField(required = False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self,commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()

        return user

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = player
#         fields = ('name', 'password',)