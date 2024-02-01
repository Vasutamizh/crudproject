from django import forms
from .models import Employee_Model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Emp_Form(forms.ModelForm):
    class Meta:
        model= Employee_Model
        fields ="__all__"



class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)