# Generated by Django 4.0.6 on 2022-07-16 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('cadastro', models.DateField(verbose_name='Data de Cadastro')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60, verbose_name='Titulo')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('editora', models.CharField(max_length=40, verbose_name='Editora')),
                ('quantidade', models.IntegerField(default=0)),
                ('publicacao', models.DateField(verbose_name='Data de Publicação')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.autor')),
            ],
            options={
                'verbose_name': 'Titulo',
                'verbose_name_plural': 'Titulos',
            },
        ),
    ]
