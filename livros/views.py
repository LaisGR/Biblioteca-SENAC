from django.shortcuts import render, redirect
from .models import Livro
from django.views import generic
from .forms import LivroForm, AutorForm
# Create your views here.

def index(request):
    return render(request, 'index.html')


def listar(request):
    lista = Livro.objects.all()
    return render(request, 'listar.html', {'livros':lista})


def cadastrar(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            return redirect('/')
    else:
        form = LivroForm()
    return render(request, 'cadastrar.html', {'form': form})            


def detalhar(request, id):
    livro = Livro.objects.get(pk=id)
    return render(request, 'detalhar.html', {'livro': livro})


def atualizar(request, id):
    livro = Livro.objects.get(pk=id)
    form = LivroForm(instance=livro)
    if (request.method == 'POST'):
        form = LivroForm(request.POST, instance=livro)
        if(form.is_valid()):
            livro.save()
            return redirect('/')
        else:
            return render(request, 'atualizar.html', {'form':form})    
    else:
        return render(request, 'atualizar.html', {'form':form})    


def deletar(request, id):
    livro = Livro.objects.get(pk=id)
    livro.delete()
    return redirect('/listar/')


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class ListView(generic.ListView):
    model = Livro
    template_name = 'listar.html'
    context_object_name = 'livros'


class CadastroView(generic.CreateView):
    model = Livro
    template_name = 'cadastrar.html'
    form_class = LivroForm
    success_url = '/'


class DetalharView(generic.DetailView):
    model = Livro
    template_name = 'detalhar.html'
    context_object_name = 'livro'


class AtualizarView(generic.UpdateView):
    model = Livro
    template_name = 'atualizar.html'
    form_class = LivroForm
    success_url = '/'    


class DeletarView(generic.DeleteView):
    model = Livro
    template_name = 'deletar.html'
    success_url = '/listar'    
    context_object_name = 'livro'