from django import forms
from .models import Crear
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegistroUserForm(UserCreationForm):
    class Meta: 
        model=User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class crearform(forms.ModelForm):
    class Meta:
        model = Crear
        fields = ['codigo', 'nombre', 'precio', 'stock', 'imagen']
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder': 'Ingrese un Codigo', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese un Nombre', 'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'placeholder': 'Ingrese un Precio', 'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'placeholder': 'Ingrese el Stock', 'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'codigo': "codigo",
            'nombre': "nombre",
            'precio': "Precio",
            'stock': "Stock",
            'imagen': "Imagen",
        }