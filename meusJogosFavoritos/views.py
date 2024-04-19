from django.shortcuts import redirect, render, get_object_or_404
from .models import Jogo, Referencia
from .forms import JogoForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def inicio(request):
  return render(request, "inicio.html")


def login_usuario(request):
  form = AuthenticationForm()
  if request.method == "POST" and request.POST:
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect("/home")
  return render(request,"login.html",{"formulario": form})

@login_required
def home(request):

  jogos = Jogo.objects.order_by("rank").filter(usuario=request.user).all()

  return render(request, 'home.html', {"jogos": jogos})

@login_required
def jogos(request, ranking):

  jogo = get_object_or_404(Jogo, rank=ranking, usuario=request.user)

  return render(request, 'jogos.html', {"jogo": jogo})

@login_required
def newJogo(request):
  formulario = JogoForm()

  if request.method == "POST" and request.POST:
    formulario = JogoForm(request.POST)

    if formulario.is_valid():
      jogo = formulario.save(commit=False)
      jogo.usuario = request.user
      jogo.save()
      return redirect("/home")

  return render(request, "newjogo.html", {"formulario": formulario})

@login_required
def editJogo(request, id):
  jogo = get_object_or_404(Jogo, pk=id, usuario=request.user)
  formulario = JogoForm(instance=jogo)

  if request.method == "POST" and request.POST:
    formulario = JogoForm(request.POST, instance=jogo)

    if formulario.is_valid():
      formulario.save()
      return redirect("/home")

  return render(request, "editjogo.html", {"formulario": formulario})

@login_required
def delJogo(request, id):
  jogo = get_object_or_404(Jogo, pk=id, usuario=request.user)

  if request.method == "POST" and request.POST:
    jogo.delete()
    return redirect("/home")

  return render(request, "deljogo.html", {"jogo": jogo})

@login_required
def logout_usuario(request):
  logout(request)
  return redirect("/")