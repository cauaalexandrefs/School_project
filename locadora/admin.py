from django.contrib import admin
from .models import Categoria, Cliente, Locacao, Filme

# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'cliente')


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'categoria')
