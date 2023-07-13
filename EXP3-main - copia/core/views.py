from imaplib import _Authenticator
from os import login_tty
from django.shortcuts import render, redirect

from core.compra import Carro
from .forms import RegistroUserForm, crearform
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

def agregar_producto(request,id):
    carrito_compra= Carro(request)
    crear = Crear.objects.get(codigo=id)
    carrito_compra.agregar(crear=crear)
    return redirect ('tienda')

def eliminar_producto(request,id):
    carrito_compra= Carro(request)
    crear = Crear.objects.get(codigo=id)
    carrito_compra.eliminar(crear=crear)
    return redirect ('tienda')

def restar_producto(request,id):
    carrito_compra= Carro(request)
    crear = Crear.objects.get(codigo=id)
    carrito_compra.restar(crear = crear)
    return redirect ('tienda')

def limpiar_producto(request,id):
    carrito_compra= Carro(request)
    crear = Crear.objects.get(codigo=id)
    carrito_compra.limpiar(crear=crear)
    return redirect ('tienda')

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario=RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=_Authenticator(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login_tty(request,user)
            return redirect ('index')
        data["form"]=formulario   
    return render(request,'registrar.html', data)


@staff_member_required
def modificar(request,id):
    productoModificado = Crear.objects.get(patente=id)
    datos ={
        'form': crearform(instance=productoModificado)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizados
        formulario = crearform(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('products')
    return render(request,'modificar.html', datos)
