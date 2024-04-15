from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegisterForm(UserCreationForm):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]*$', 'Only alphanumeric characters and underscores are allowed.')
    username = forms.CharField(validators=[alphanumeric])
    
    email = forms.EmailField(required=True)

    class Meta :
        model = User
        fields = ['username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email


class UserUpdateForm(forms.ModelForm):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z_]*$', 'Only alphanumeric characters and underscores are allowed.')
    username = forms.CharField(validators=[alphanumeric])
    
    email = forms.EmailField()
    
    class Meta :
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta :
        model = Profile
        fields = ['image']
