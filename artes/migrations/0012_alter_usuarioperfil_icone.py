# Generated by Django 5.0 on 2023-12-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artes', '0011_alter_usuarioperfil_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioperfil',
            name='icone',
            field=models.ImageField(blank=True, default='https://cdn.icon-icons.com/icons2/788/PNG/512/user-1_icon-icons.com_65106.png', null=True, upload_to='midia'),
        ),
    ]