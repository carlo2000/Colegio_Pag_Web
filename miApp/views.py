from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'miApp/index.html')
def institucion(request):
    return render(request,'miApp/institucion.html')
def galeria(request):
    return render(request,'miApp/galeria.html')