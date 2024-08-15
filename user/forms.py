from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['initials', 'unique', 'address', 'idnum', 'cell', 'homenum', 'dob', 'designation', 'image']
        widgets={
            'dob': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)
