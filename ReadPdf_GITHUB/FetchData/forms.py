from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django import forms



class GetPattern(forms.Form):
    pattern=forms.CharField(label='Enter Pattern/Word : ', widget=forms.TextInput(attrs={'style': 'border-color: green', 'placeholder': 'Pattern'}), required=False)
    source_file_path=forms.CharField(label='Enter Source/Path : ', widget=forms.TextInput(attrs={'style': 'border-color: green', 'placeholder': 'Source/Path'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='Username : ',widget=forms.TextInput(attrs={'style': 'border-color: green', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password : ', widget=forms.TextInput(attrs={'style': 'border-color: green', 'placeholder': 'Password'}))

