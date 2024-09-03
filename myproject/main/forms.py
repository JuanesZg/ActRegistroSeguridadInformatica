from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if not re.match(r'^[\w]+$', password):
            raise forms.ValidationError('La contraseña solo puede contener caracteres alfanuméricos.')
        return password
