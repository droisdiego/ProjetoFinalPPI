from django.db import models
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

User = get_user_model()

class UsuarioPerfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pseudonimo = models.CharField(max_length=50)
    nome_social = models.CharField(max_length=50, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    icone = models.ImageField(upload_to='midia', default='midia/abstract-user-flat-3.png',null=True, blank=True)

    def get_email(self):
        return EmailAddress.objects.get(user=self.usuario).email if EmailAddress.objects.filter(user=self.usuario, primary=True, verified=True).exists() else None
    
    def __str__(self):
        return f"{self.usuario.username}"
    

class Publicacao(models.Model):
    autor = models.ForeignKey(UsuarioPerfil, on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='uploads/', null=True, blank=True)
    imagem = models.ImageField(upload_to='uploads/', null=True, blank=True)
    video = models.FileField(upload_to='uploads/', null=True, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id} - {self.texto[:20]}"


class Favoritos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacoes_salvas = models.ManyToManyField(Publicacao)


class Denuncia(models.Model):
    publicacao_denunciada = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    autor_denuncia = models.ForeignKey(User, on_delete=models.CASCADE)
    motivo = models.TextField()
    data_denuncia = models.DateTimeField(auto_now_add=True)


class Comunidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunidades_criadas')
    membros = models.ManyToManyField(User, related_name='comunidades_membro')


class Followers(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
