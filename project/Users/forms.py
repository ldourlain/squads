from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Administrator


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Administrator
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Administrator
        fields = ('username', 'email')