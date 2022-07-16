"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from livros.views import  IndexView, ListView, CadastroView, DetalharView, AtualizarView, DeletarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='livros_index'),
    path('listar/', ListView.as_view(), name='livros_listar'),
    path('cadastrar/', CadastroView.as_view(), name='livros_cadastrar'),
    path('<int:pk>', DetalharView.as_view(), name='livros_detalhar'),
    path('atualizar/<int:pk>', AtualizarView.as_view(), name='livros_atualizar'),
    path('deletar/<int:pk>', DeletarView.as_view(),name='livros_deletar'),
]
