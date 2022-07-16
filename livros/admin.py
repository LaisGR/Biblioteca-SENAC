from django.contrib import admin
from .models import Autor, Livro
# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cadastro')


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'editora', 'quantidade', 'publicacao', 'autor')