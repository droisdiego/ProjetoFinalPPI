# Generated by Django 5.0 on 2023-12-13 03:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artes', '0002_comunidade_denuncia_usuarioperfil'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pasta',
            new_name='Favoritos',
        ),
    ]