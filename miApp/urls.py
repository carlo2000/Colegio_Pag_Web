from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='index'),
    path('institucion/', views.institucion, name='institucion'),
    path('galeria/', views.galeria, name='galeria'),
    
]