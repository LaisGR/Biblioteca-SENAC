from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Livro, Autor

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'descricao', 'editora', 'quantidade', 'publicacao', 'autor']

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'cadastro']