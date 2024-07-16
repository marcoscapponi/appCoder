from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "appCoder/inicio.html")

def cursos(request):
    return HttpResponse("Vista de los cursos")

def estudiantes(request):
    return HttpResponse("Vista de los estudiantes")

def profesores(request):
    return HttpResponse("Vista de los profesores")

def entregables(request):
    return HttpResponse("Vista de los entregables")