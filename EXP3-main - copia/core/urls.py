from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('crear/', views.crear_views, name='crear'),
    path('modificar/<id>', views.modificar, name="modificar"),
    path('registrar/',views.registrar,name="registrar"),
    path('mostrar/',views.mostrar, name="mostrar"),
    

]
