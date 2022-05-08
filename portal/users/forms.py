from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username',
        'placeholder': 'Foydalanuvchi ismi'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password',
        'placeholder': 'Parol'
    }))



class RegistrationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'photo',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form__inp',
                'placeholder': 'Login',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form__inp',
                'placeholder': 'Ism'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form__inp',
                'placeholder': 'Familiya'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form__inp',
                'placeholder': 'Email',
            }),
        }













