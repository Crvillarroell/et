from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('crear/', views.crear_views, name='crear'),
    path('mostrar/',views.mostrar, name="mostrar"),
    

]
