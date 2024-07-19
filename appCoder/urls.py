from django.urls import path
from appCoder.views import *




urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos', cursos, name="cursos"),
    path('estudiantes', estudiantes, name="estudiantes"),
    path('profesores', profesores, name="profesores"),
    path('entregables', entregables, name="entregables"),
]