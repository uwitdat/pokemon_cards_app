from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
from .forms import AbillityForm


class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = '__all__'


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})


def pokemon_detail(request, poke_id):
    poke = Pokemon.objects.get(id=poke_id)
    items_poke_doesnt_have = Item.objects.exclude(
        id__in=poke.items.all().values_list('id'))
    ability_form = AbillityForm()
    return render(request, 'pokemon/detail.html', {'poke': poke,
                                                   'ability_form': ability_form, 'items': items_poke_doesnt_have})


def add_ability(request, poke_id):
    form = AbillityForm(request.POST)
    if form.is_valid():
        new_ability = form.save(commit=False)
        new_ability.poke_id = poke_id
        new_ability.save()
    return redirect('detail', poke_id=poke_id)


class ItemList(ListView):
    model = Item


class ItemDetail(DetailView):
    model = Item


class ItemCreate(CreateView):
    model = Item
    fields = '__all__'


class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'


class ItemDelete(DeleteView):
    model = Item
    success_url = '/items/'


def assoc_item(request, poke_id, item_id):
    Pokemon.objects.get(id=poke_id).items.add(item_id)
    return redirect('detail', poke_id=poke_id)
