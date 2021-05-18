from django.forms import ModelForm
from .models import Ability


class AbillityForm(ModelForm):
    class Meta:
        model = Ability
        fields = ['ability']
