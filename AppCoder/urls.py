from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio, name= "Inicio"),
    path("cursos/", curso, name= "Cursos"),
    path("productos/", productos, name= "Productos"),
    path("turnos/", turnos, name= "Turnos"),
    path("formu1/", formulario1, name= "Formulario Cursos"),
    path("formu2/", formulario2, name= "Formulario Turnos"),
    path("formu3/", formulario3, name= "Formulario Productos"),
    path("buscarCursos/", busquedaCursos),
    path("buscar/", buscar),
]

# Le doy nombre para linkearlo con una vista
