from django.contrib import admin
from .models import Jogo, Referencia

# Register your models here.

class JogoAdm(admin.ModelAdmin):
  list_display = ["nome","icone","rank","descricao","data_lancamento","nota"]

  ordering = ["rank"]

admin.site.register(Jogo, JogoAdm)

class ReferenciaAdm(admin.ModelAdmin):
  list_display = ["jogo","nome","link","tipo","favorito"]

  ordering = ["favorito","jogo"]

admin.site.register(Referencia, ReferenciaAdm)