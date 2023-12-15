from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from artes.forms import *
from artes.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch import receiver


User = get_user_model()


class HomeView(generic.ListView):
    model = Publicacao
    template_name = "index.html"
    ordering = ['-data_publicacao']
    context_object_name = 'publicacoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicione informações do usuário ao contexto
        if self.request.user.is_authenticated:
            usuario_perfil = UsuarioPerfil.objects.get(usuario=self.request.user)
            context['usuario_perfil'] = usuario_perfil

        return context

class PublicacaoCreateView(generic.CreateView):
    model = Publicacao
    form_class = PublicacaoForm
    success_url = reverse_lazy("index")
    template_name = "criar_plub.html"

    def form_valid(self, form):
       usuario_perfil = UsuarioPerfil.objects.get(usuario=self.request.user)
       form.instance.autor = usuario_perfil
       return super().form_valid(form)


class PublicacaoDeleteView(generic.DeleteView):
    model = Publicacao
    success_url = reverse_lazy("index")
    template_name = "publicacao_confirm_delete.html"


class PublicacaoUpdate(generic.UpdateView):
    model = Publicacao
    form_class = PublicacaoForm
    success_url = reverse_lazy("index")
    template_name = "criar_plub.html"


class PublicacaoDetailView(generic.DetailView):
    model = Publicacao
    template_name = "publicacao.html"


class ProfileView(generic.DetailView):
    model = User
    template_name = "profile.html"
    slug_field = "usuario"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user_object = self.get_object()
        usuario_perfil = get_object_or_404(UsuarioPerfil, usuario=user_object)
        user_posts = Publicacao.objects.filter(autor=usuario_perfil).order_by("-data_publicacao")

        context["user_posts"] = user_posts
        context["profile_user"] = user_object
        context["usuario_perfil"] = usuario_perfil
        return context


class UsuarioPerfilUpdateView(generic.UpdateView):
    model = UsuarioPerfil
    form_class = UsuarioPerfilForm  
    template_name = 'profile_upload.html'  
    success_url = reverse_lazy('index')  
    

@receiver(user_signed_up)
@receiver(user_logged_in)
def criar_usuario_perfil(request, user, **kwargs):
    if not UsuarioPerfil.objects.filter(usuario=user).exists():
        UsuarioPerfil.objects.create(usuario=user)



def pesquisa(request):
    username = request.GET.get('username')
    resultados = []

    if username:
        print(f'Pesquisando por: {username}')
        resultados = UsuarioPerfil.objects.filter(usuario__username__icontains=username)

    return render(request, 'usuarios.html', {'resultados': resultados, 'termo_pesquisa': username})

def usuarios(request):
    lista = UsuarioPerfil.objects.order_by('-id')
    return render(request, 'usuarios.html', {'resultados': lista})