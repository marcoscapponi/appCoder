from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "appCoder/inicio.html")

def cursos(request):
    return render(request, "appCoder/cursos.html")

def estudiantes(request):
    return render(request, "appCoder/estudiantes.html")

def profesores(request):
    return render(request, "appCoder/profesores.html")

def entregables(request):
    return render(request, "appCoder/entregables.html")