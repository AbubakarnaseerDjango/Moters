from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import Contact
from django.contrib.auth.models import User
class ContactModelForm(forms.ModelForm):
     class Meta:
        model = Contact
        fields = '__all__'

class CreatUserForm(UserCreationForm,forms.Form):
    first_name = forms.CharField(max_length = 20,error_messages={'required':'Enter First Name'})
    last_name = forms.CharField(max_length = 20 , error_messages = {'required' : 'Enter Last Name'})

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2',]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','is_active']