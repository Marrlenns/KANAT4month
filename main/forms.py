from django import forms
from django.core.exceptions import ValidationError

from .models import *


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if Film.objects.filter(title=title).count() > 0:
            raise ValidationError("Film with this title already exists!!!\nFilm's title must be UNIQUE!!!")
        return title


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(name=name).count() > 0:
            raise ValidationError("Director with this name already exists!!!\nDirector's name must be UNIQUE!!!")
        return name
