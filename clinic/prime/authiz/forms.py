from django import forms
# from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Client
from .utils import number_prettify

class SignUpForm(forms.Form):
    phone = forms.CharField(label='Номер телефона', help_text='Required. Inform a valid email address.', 
                    widget=forms.TextInput(attrs={'placeholder': '(996) ___-__-__-__','class':"uk-input phone_us"}))

    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput())

    agree_1 = forms.BooleanField()
    agree_2 = forms.BooleanField()

    def clean(self):
        
        if not self.cleaned_data['agree_1']:
            raise forms.ValidationError('You have to agree to out privacy temrs 1')
        
        if not self.cleaned_data['agree_2']:
            raise forms.ValidationError('You have to agree to out privacy temrs 2')
        
        password1 = self.cleaned_data['password1']
        
        password2 = self.cleaned_data['password2']
        
        if password1 != password2:
            raise forms.ValidationError('Passwords must match')

        telephone = self.cleaned_data['phone']

        check_client = Client.objects.filter(phone=number_prettify(telephone)).first()
        if check_client is not None:
            raise forms.ValidationError('Number is registered')

class LoginForm(forms.Form):
    phone = forms.CharField(label='Номер телефона', help_text='Required. Inform a valid email address.', 
                    widget=forms.TextInput(attrs={'placeholder': '(996) ___-__-__-__','class':"uk-input phone_us"}))

    password = forms.CharField(label='Пароль',widget=forms.PasswordInput())
    remember_me = forms.BooleanField()

    def clean(self):

        telephone = self.cleaned_data['phone']
        password = self.cleaned_data['password']

        check_client = Client.objects.filter(phone=number_prettify(telephone)).first()
        if not check_client:
            raise forms.ValidationError('Wrong telephone or password')
        if check_client:
            if not check_client.check_password(password):
                raise forms.ValidationError('Wrong telephone or password')