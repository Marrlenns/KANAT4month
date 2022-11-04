from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
# Create your views here.


# def welcome(request):
#     return render(request, 'welcome.html')

def search(request):
    search_word = request.GET.get('search_word')
    context = {
        'search_word': search_word,
        'films': Film.objects.filter(title__icontains=search_word)
    }
    return render(request, 'search.html', context)


def register_(request):
    context = {
        'form': UserCreateForm()
    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/films/')
        context['form'] = form
    return render(request, 'register.html', context)


def login_(request):
    context = {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/films/')
            else:
                return redirect('/login/')
    return render(request, 'login.html', context)

def create_film(request):
    context = {
        'form': FilmForm()
    }
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
        else:
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
            return redirect('/directors/')
        else:
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


PAGE_SIZE = 3


def films(request):
    page = int(request.GET.get('page', 1))
    all_films = Film.objects.all()
    films = all_films[(page - 1) * PAGE_SIZE: page * PAGE_SIZE]
    pages = (all_films.count() + PAGE_SIZE - 1) // PAGE_SIZE
    # if all_films.count() % PAGE_SIZE:
    #     page = all_films.count() // PAGE_SIZE
    # else:
    #     page = all_films.count() // PAGE_SIZE + 1

    data = {
        'films': films,
        'buttons': [i for i in range(1, pages + 1)],
        'prev_page': page - 1,
        'next_page': page + 1,
        'page': page,
        'pages': pages
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
    except Film.DoesNotExist:
        return HttpResponse("Director not found")
    data = {
        'director': director,
        'films': films
    }
    return render(request, 'director_films.html', data)


# def search(request):
#     search_word = request.GET.get('search_word', '')
#     context = {
#         'films': Film.objects.filter(title__icontains=search_word).order_by('title').exclude(rating=0),
#         'search_word': search_word
#     }
#     return render(request, 'search.html', context)
