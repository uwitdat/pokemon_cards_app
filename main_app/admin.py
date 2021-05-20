from django.contrib import admin
from .models import Pokemon, Ability, Item

# Register your models here.
admin.site.register(Pokemon)

admin.site.register(Ability)

admin.site.register(Item)
