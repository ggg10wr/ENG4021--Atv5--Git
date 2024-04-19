from django.shortcuts import redirect, render
from .models import Jogo, Referencia
from .forms import JogoForm

# Create your views here.

def home(request):

  jogos = Jogo.objects.order_by("rank").all()
  
  return render(request, 'home.html',{"jogos": jogos})


def jogos(request, ranking):

  jogo = Jogo.objects.get(rank=ranking)

  return render(request, 'jogos.html',{"jogo": jogo})

def newJogo(request):
  formulario = JogoForm()

  if request.method == "POST" and request.POST:
    formulario = JogoForm(request.POST)

    if formulario.is_valid():
      formulario.save()
      return redirect("/")

  return render(request,"newjogo.html",{"formulario": formulario})

def editJogo(request,id):
  jogo = Jogo.objects.get(pk=id)
  formulario = JogoForm(instance=jogo)

  if request.method == "POST" and request.POST:
    formulario = JogoForm(request.POST, instance=jogo)

    if formulario.is_valid():
        formulario.save()
        return redirect("/")

  return render(request,"editjogo.html",{"formulario": formulario})

def delJogo(request,id):
  jogo = Jogo.objects.get(pk=id)

  if request.method == "POST" and request.POST:
    jogo.delete()
    return redirect("/")

  return render(request,"deljogo.html",{"jogo": jogo})