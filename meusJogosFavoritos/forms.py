from django import forms
from django.db.models import fields
from .models import Jogo, Referencia

class JogoForm(forms.ModelForm):
  class Meta:
    model = Jogo
    exclude = ["usuario"]