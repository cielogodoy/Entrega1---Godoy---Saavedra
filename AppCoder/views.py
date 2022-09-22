from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import FormularioCurso, FormularioProductos, FormularioTurno
from AppCoder.models import *

# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def productos(request):
    return render(request, "AppCoder/productos.html")

def curso(request):
    #curso2= Cursos(nombre="Diseño", camada=12345)
    #curso2.save()
    return render(request, "AppCoder/cursos.html")

def turnos(request):
    return render(request, "AppCoder/turnos.html")


def formulario1(request):
    if request.method == "POST": # si le doy click en ENVIAR

        formulario1= FormularioCurso(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cursoF = Cursos(nombre=info["nombre"], camada=info["camada"]) # si los recuadros de texto están completos
            cursoF.save()            
            return render (request, "AppCoder/inicio.html") # lleva al inicio después de presionar GO
    else:
        formulario1=FormularioCurso() # muestra formulario vacio
    return render (request, "AppCoder/formu1.html" , {"form1": formulario1})  #en la vista creo el formulario y lo mando al html, si uso la clave sino presiono enviar tambien quiero ver vacía

def formulario2(request):
    if request.method == "POST": 
        formulario2= FormularioTurno(request.POST)

        if formulario2.is_valid():
            info2 = formulario2.cleaned_data
            # me fijo en el modelo que busca, en este caso Profesor [EL NOMBRE QUE LE DI EN EL FORMULARIO en forms.py]
            turnoF = Turnos(servicio=info2["servicio"], nombre=info2["nombre"],fechaTurno=info2["fechaTurno"]) # si los recuadros de texto están completos
            turnoF.save()            
            return render (request, "AppCoder/inicio.html") 
    else:
        formulario2=FormularioTurno() # muestra formulario vacio
    return render (request, "AppCoder/formu2.html" , {"form2": formulario2})  #en la vista creo el formulario y lo mando al html, si uso la clave sino presiono enviar tambien quiero ver vacía

def formulario3(request):
    if request.method == "POST": 
        formulario3= FormularioProductos(request.POST)

        if formulario3.is_valid():
            info3 = formulario3.cleaned_data
            # me fijo en el modelo que busca, en este caso Profesor [EL NOMBRE QUE LE DI EN EL FORMULARIO en forms.py]
            prodF = Productos(nombre=info3["nombre"], marca=info3["marca"]) # si los recuadros de texto están completos
            prodF.save()            
            return render (request, "AppCoder/inicio.html") 
    else:
        formulario3=FormularioProductos() # muestra formulario vacio
    return render (request, "AppCoder/formu3.html" , {"form3": formulario3})  #en la vista creo el formulario y lo mando al html, si uso la clave sino presiono enviar tambien quiero ver vacía

def busquedaCursos(request):
    return render(request, "AppCoder/busquedaCursos.html")


def buscar(request):
    #busqueda=request.GET["camada"]
    #return HttpResponse(f"Camada {busqueda}")
    if request.GET["camada"]:
        busqueda=request.GET["camada"]
        cursos=Cursos.objects.filter(camada__iexact=busqueda)
        return render (request, "AppCoder/inicio.html", {"cursos":cursos, "busqueda": busqueda})
    else:
        mensaje="No se cargan datos"
    
    return HttpResponse(mensaje)