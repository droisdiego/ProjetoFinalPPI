"""
URL configuration for onuarte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from artes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',HomeView.as_view(),name='index'),

    path('criar_publicacao/', PublicacaoCreateView.as_view(), name='criar_publicacao'),
    path('publicacao/<int:pk>/delete/', PublicacaoDeleteView.as_view(), name='publicacao_delete'),
    path('publicacao/<int:pk>/editar/', PublicacaoUpdate.as_view(), name='editar_publicacao'),
    path('publicacao/detail/<int:pk>/', PublicacaoDetailView.as_view(), name='publicacao_detalhe'),

    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('perfil/editar/<int:pk>', UsuarioPerfilUpdateView.as_view(), name='editar_perfil'),

    path('usuarios/', pesquisa, name='pesquisa'),

    path('perfil/<str:username>/', ProfileView.as_view(), name='profile'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
