from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), label='D.O.B')
    phone_number = forms.CharField(max_length=50, required=False, label='Phone Number')
    email = forms.CharField(max_length=254, required=True)
    
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'dob', 'phone_number', 'email', 'password1', 'password2')
        labels = {
            "username" : "Username",
            "email" : "Email",
            "password1": "Password",
            "password2" : "Re-enter Password",
        }