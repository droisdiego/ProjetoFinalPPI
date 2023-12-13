from django.contrib import admin
from .models import *

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('autor', 'texto', 'data_publicacao')

@admin.register(Favoritos)
class PastaAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

@admin.register(UsuarioPerfil)
class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pseudonimo', 'nome_social')

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('publicacao_denunciada', 'autor_denuncia', 'motivo', 'data_denuncia')

@admin.register(Comunidade)
class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'criador')
    filter_horizontal = ('membros',)