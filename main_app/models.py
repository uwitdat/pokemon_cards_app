from django.db import models
from django.urls import reverse
import random
from django.contrib.auth.models import User

# Create your models here.
ABILITIES = (
    ('A', 'Growl'),
    ('B', 'Take Down'),
    ('C', 'Tackle'),
    ('D', 'Rest'),
    ('E', 'Protect'),
    ('F', 'Special Attack'),
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    description = models.TextField(
        max_length=250,
        default='none'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items_detail', kwargs={'pk': self.id})


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default='none')
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.name

    def save(self):
        self.type = self.type.lower()
        return super(Pokemon, self).save()

    def average(self):
        sum = (self.hp + self.attack + self.defense +
               self.sp_attack + self.sp_defense + self.speed) / 6
        average = round(sum)
        return average

    def total(self):
        total = self.hp + self.attack + self.defense + \
            self.sp_attack + self.sp_defense + self.speed
        return total

    def get_absolute_url(self):
        return reverse('detail', kwargs={'poke_id': self.id})

    def upper(self):
        upper = self.user.upper()
        return upper

    class Meta:
        ordering = ['name']


class Ability(models.Model):
    ability = models.CharField(
        max_length=1,
        choices=ABILITIES,
        default=ABILITIES[0][0]
    )

    poke = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_ability_display()}'

    def power(self):
        power = self.poke.total()
        rand_num = random.randint(50, power)
        return rand_num

    def accuracy(self):
        rand_num = random.randint(10, 100)
        return rand_num
