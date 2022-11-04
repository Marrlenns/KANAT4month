from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from .forms import *
# Create your views here.


# def welcome(request):
#     return render(request, 'welcome.html')


def create_film(request):
    context = {
        'form': FilmForm()
    }
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/films/")
        context['form'] = form
    return render(request, 'create_film.html', context)


def create_director(request):
    context = {
        'form': DirectorForm()
    }
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/directors/")
        context['form'] = form
    return render(request, 'create_director.html', context)


def about(request):
    data = {
        'about': "Kaif Sait"
    }
    return render(request, 'about.html', data)


def date_(request):
    data = {
        'date': datetime.now()
    }
    return render(request, 'datetime.html', data)


def films(request):
    data = {
        'films': Film.objects.all()
    }
    return render(request, 'films.html', data)


def directors(request):
    data = {
        'directors': Director.objects.all()
    }
    return render(request, 'directors.html', data)


def one_film(request, id):
    try:
        film = Film.objects.get(id=id)
    except:
        return HttpResponse("Film not found")
    data = {
        'film': film
    }
    return render(request, 'one_film.html', data)


def director_films(request, director_id):
    try:
            director = Director.objects.get(id=director_id)
            films = Film.objects.filter(director_id=director)
    except:
        return HttpResponse("Director not found")
    data = {
        'director': director,
        'films': films
    }
    return render(request, 'director_films.html', data)