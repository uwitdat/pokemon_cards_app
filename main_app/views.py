from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
from .forms import AbillityForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})


def pokemon_detail(request, poke_id):
    poke = Pokemon.objects.get(id=poke_id)
    ability_form = AbillityForm()
    return render(request, 'pokemon/detail.html', {'poke': poke, 'ability_form': ability_form})


def add_ability(request, poke_id):
    form = AbillityForm(request.POST)
    if form.is_valid():
        new_ability = form.save(commit=False)
        new_ability.poke_id = poke_id
        new_ability.save()
    return redirect('detail', poke_id=poke_id)


class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = '__all__'


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'
