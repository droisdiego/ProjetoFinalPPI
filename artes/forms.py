# artes/forms.py
from django import forms
from django.urls import reverse_lazy
from .models import *

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['texto', 'imagem']

    def clean(self):
        cleaned_data = super().clean()
        texto = cleaned_data.get('texto')
        # audio = cleaned_data.get('audio')
        imagem = cleaned_data.get('imagem')
        # video = cleaned_data.get('video')

        # Elementos de audio e video foram retirados por questão de tempo para versão 1.0, possibilidade de adição em futura atualização
        if not any([texto, imagem]):
            raise forms.ValidationError('Pelo menos um dos elementos (texto, áudio, imagem ou vídeo) deve estar presente.')
        

class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioPerfil
        fields = ['pseudonimo', 'nome_social', 'biografia', 'icone']
        success_url = reverse_lazy('profile')  # Use reverse_lazy para evitar problemas de importação circular

    def form_valid(self, form):
        # Lógica para processar o formulário
        return super().form_valid(form)