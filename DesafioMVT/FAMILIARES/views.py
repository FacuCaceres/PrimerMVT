from django.shortcuts import render
from FAMILIARES.models import Familia
# Create your views here.

def mostrarFamilia(request):

    famiares = Familia.objects.all()
    contexto = {
        'familiares':famiares
    }
    return render(request,'familia.html',contexto)