#coding=utf-8
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, Select, PasswordInput, EmailInput
from .models import *


class Register_form(ModelForm):
    class Meta:
        model = User
        fields = ['nickname','user','passwd','email','sex']
        widgets = {
            'nickname': TextInput(attrs={'class': 'form-control', 'placeholder': '张三', 'autofocus': True}),
            'user': TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}),
            'passwd': PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'abc@abc.com'}),
            'sex': Select(attrs={'class': 'form-control'}),
        }


class Login_form(ModelForm):
    class Meta:
        model = User
        fields = ['user','passwd']
        widgets = {
            'user': TextInput(attrs={'class': 'form-control', 'placeholder': '用户名', 'autofocus': True}),
            'passwd': PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}),
        }