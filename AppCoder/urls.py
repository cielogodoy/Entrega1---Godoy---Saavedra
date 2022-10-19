from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",inicio, name= "Inicio"),
    path("login/",iniciar_sesion, name= "Iniciar sesión"),
    path("registro/",registro, name= "Registro"),

    path("cursos/", curso, name= "Cursos"),
    path("leerProductos/", leerProductos, name= "Productos"),
    path("turnos/", turnos, name= "Turnos"),
    path("formu1/", formulario1, name= "Formulario Cursos"),
    path("formu2/", formulario2, name= "Formulario Turnos"),
    path("formu3/", formulario3, name= "Formulario Productos"),
    path("buscarCursos/", busquedaCursos),
    path("buscar/", buscar),
    path("borrarProductos/<produNombre>", borrarProductos, name= "borrarProductos"),
    #path("leerProductos/", leerProductos),
    path("editarProduc/<produNombre>", editarProduc, name="editarProduc"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Cerrar sesión"),
    path("editarUsuarios/", editarUsuario, name="Edición de usuarios"),
    path("aboutus/", about, name="About"),
    path("muestraUsuarios/", usuarios, name="Usuarios"),


]

# Le doy nombre para linkearlo con una vista
