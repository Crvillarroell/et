from django.shortcuts import render, redirect
from .forms import crearform
from django.contrib.admin.views.decorators import staff_member_required
from .models import Crear # Reemplaza "CrearModelo" con el nombre correcto de tu modelo


def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

@staff_member_required
def products(request):
    return render(request, 'core/products.html')

@staff_member_required
def crear_views(request):
    if request.method == "POST":
        form = crearform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core_index')
    else:
        form = crearform()

    return render(request, 'core/crear.html', {'crearform': crearform})

def mostrar(request):
    jardineria = crear_views.objects.all() 
    datos = {
        'jardineria': jardineria
    }
    return render(request, 'core/mostrar.html', datos)

