from tabnanny import verbose
from pyexpat import model
from django.db import models

# Create your models here.
class Autor(models.Model):
        nome = models.CharField('Nome', max_length=40)
        cadastro = models.DateField('Data de Cadastro')

        def __str__(self):
            return self.nome 

        class Meta:
            verbose_name = 'Autor'
            verbose_name_plural = 'Autores'     


class Livro(models.Model):
        titulo = models.CharField('Titulo', max_length=60)
        descricao = models.CharField('Descrição', max_length=100)
        editora = models.CharField('Editora', max_length=40)
        quantidade = models.IntegerField(default=0)
        publicacao = models.DateField('Data de Publicação')
        autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

        def __str__(self):
            return self.titulo 

        class Meta:
            verbose_name = 'Livro'
            verbose_name_plural = 'Livros'      