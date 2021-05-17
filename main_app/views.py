from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})


def pokemon_detail(request, poke_id):
    poke = Pokemon.objects.get(id=poke_id)
    return render(request, 'pokemon/detail.html', {'poke': poke})
