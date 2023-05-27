from django.shortcuts import render
from .models import Locacao, Filme

# Create your views here.


def index(request):
    return render(request, 'locacao/index.html')


def locacao(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locacao/locacao.html', {'locacoes': locacoes})


def filme(request):
    filmes = Filme.objects.all()
    return render(request, 'locacao/filmes.html', {'filmes': filmes})