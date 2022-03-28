from re import A
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor

# Create your views here.
def home(request):
    return render(request, 'index.html')

# Función para crear autores de libros 
def crear_autor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            print(autor_form)
            return redirect('libro:listar_autor')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})

def listar_autor(request):
    autores = Autor.objects.filter(estado = True)
    return render(request, 'libro/listar_autor.html', {'autores':autores})

def editar_autor(request, id):
    error = None
    autor_form = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')
    except ObjectDoesNotExist as e:
        error = e        
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error':error})


def eliminar_autor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')

    return render(request, 'libro/eliminar_autor.html', {'autor':autor})
