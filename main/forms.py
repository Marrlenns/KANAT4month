from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from . import models


class FilmForm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields = "__all__"

    def clean_title(self):
        title = self.clean_data['title']
        if models.Film.Objects.filter(title=title):
            raise ValidationError("Film already exists!!!")
        return title


class DirectorForm(forms.ModelForm):
    class Meta:
        model = models.Director
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if models.Director.objects.filter(name=name):
            raise ValidationError('Director with this name already exists')
        return name


class UserCreateForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError("User with this username already exists!!!")
        return username

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise ValidationError("Passwords does not match!!1")
        return password1


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
