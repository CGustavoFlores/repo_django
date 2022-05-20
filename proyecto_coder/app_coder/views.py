from typing import TextIO
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template  import loader




# Create your views here.
def inicio(request):
    return render(request , "plantillas.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc= {"cursos": cursos}
    plantilla =loader.get_template("plantillas.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

    
def alta_curso(Request,nombre):
    curso = Curso(nombre= nombre,camada=5255)
    curso.save()
    texto = f"Se guardo en la bd el curso : {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)
    