from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class Pokemon:

    average = 0

    def __init__(self, name, hp, attack, defense, sp_attack, sp_defense, speed):
        self.name = name.upper()
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.total = hp + attack + defense + sp_attack + sp_defense + speed

    def average(self):
        sum = (self.hp + self.attack + self.defense +
               self.sp_attack + self.sp_defense + self.speed) / 6
        average = round(sum)
        return average


pokemon = [
    Pokemon('Charizard', 78, 84, 78, 109, 85, 100),
    Pokemon('Blastoise', 79, 83, 100, 85, 105, 78),
    Pokemon('Jigglypuff', 115, 45, 20, 45, 25, 20)
]


def home(request):
    return HttpResponse("<a href='/about'>About</a>")


def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})
