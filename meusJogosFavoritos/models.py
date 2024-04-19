from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Jogo(models.Model):
  nome = models.CharField(max_length=50)
  icone = models.URLField(max_length=1000)
  rank = models.IntegerField()
  descricao = models.TextField()
  data_lancamento = models.DateField()
  nota = models.DecimalField(max_digits=3, decimal_places=1)

  def __str__(self):
    return self.nome


class Referencia(models.Model):
  jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
  nome = models.CharField(max_length=100)
  link = models.URLField(max_length=1000)
  tipo = models.CharField(max_length=2,
    choices = {
      "pg": "Pagina do jogo",
      "wk": "Wiki do Jogo",
      "vi": "Video do jogo",
      "jo": "Jogo na internet",
      "ou": "Outros"
    })
  favorito = models.BooleanField()

  def __str__(self):
    return self.nome