from django.db import models

# Create your models here.
ABILITIES = (
    ('A', 'Growl'),
    ('B', 'Take Down'),
    ('C', 'Tackle'),
    ('D', 'Rest'),
    ('E', 'Protect'),
    ('F', 'Special Attack'),
)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default='none')
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()

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
