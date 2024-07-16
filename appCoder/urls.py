from django.urls import path
from appCoder.views import *




urlpatterns = [
    path('pagina-inicio', inicio),
    path('pagina-cursos', cursos),
    path('pagina-estudiantes', estudiantes),
    path('pagina-profesores', profesores),
    path('pagina-entregables', entregables),
]