from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
#from django.contrib.auth.mixins import LoginRequiredMixin la misma idea e el required, pero lo uso para las clases 
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    #avatares= Avatar.objects.filter(user=request.user.id)
    #contexto= {"url": avatares[0].imagen.url}
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

@login_required
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

def leerProductos(request):
    products= Productos.objects.all()
    contexto={'products': products}
    return render(request, "AppCoder/productos.html",contexto )

def borrarProductos(request, produNombre):
    produc= Productos.objects.get(nombre=produNombre)
    produc.delete()
    products= Productos.objects.all()
    contexto={'products': products}
    return render(request, "AppCoder/productos.html",contexto )

def editarProduc(request, produNombre):
    produc= Productos.objects.get(nombre=produNombre)
    if request.method == "POST": 
        formulario3= FormularioProductos(request.POST)

        if formulario3.is_valid():
            info3 = formulario3.cleaned_data
            #prodF = Productos(nombre=info3["nombre"], marca=info3["marca"]) # si los recuadros de texto están completos
            #prodF.save()            
            produc.nombre= info3["nombre"]
            produc.marca= info3["marca"]
            produc.save()
            return render (request, "AppCoder/inicio.html") 
    else:
        formulario3=FormularioProductos(initial={"nombre": produc.nombre, "marca": produc.marca}) # no muestra formulario vacio, muestra los valores antiguos del producto
   
    contexto = {"form3": formulario3, "produNombre": produNombre}
    return render (request, "AppCoder/editarProduc.html" , contexto)
    
def iniciar_sesion(request):


      if request.method == "POST":
            form5 = AuthenticationForm(request, data = request.POST)

            if form5.is_valid():
                  usuario = form5.cleaned_data.get('username')
                  contra = form5.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"¡Hola {usuario}!"} )
                  else:
                        
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form5 = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form5':form5} )

def registro(request):

      if request.method == 'POST':

            form6 = FormularioRegistro(request.POST)
            #form6 = UserCreationForm(request.POST)

            if form6.is_valid():

                  username = form6.cleaned_data['username']
                  form6.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"Usuario Creado con éxito. ¡Hola {username}!"})


      else:
            form6 = FormularioRegistro()   
            #form6 = UserCreationForm()     
  

      return render(request,"AppCoder/registro.html" ,  {"form6":form6})

@login_required
def editarUsuario(request):

    usuarioConectado = request.user

    if request.method == "POST": 

        miFormulario= FormularioEditarUsuario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data
                     
            usuarioConectado.first_name= info["first_name"]
            usuarioConectado.last_name= info["last_name"]

            usuarioConectado.email= info["email"]
            usuarioConectado.password1= info["password1"]
            usuarioConectado.password2= info["password2"]
            usuarioConectado.first_name= info["first_name"]
            usuarioConectado.last_name= info["last_name"]

            usuarioConectado.save()
            return render (request, "AppCoder/inicio.html") 
    else:
        miFormulario=FormularioEditarUsuario(initial={"email": usuarioConectado.email}) 

    contexto6 = {"miForm": miFormulario, "email": usuarioConectado}
    return render (request, "AppCoder/editarUsuarios.html" , contexto6)

'''
@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form7 =AvatarFormulario(request.POST, request.FILES)
        if form7.is_valid():
            usuarioActual=User.objects.get(username=request.user)
            avatar7 = Avatar(user=usuarioActual, imagen=form7.cleaned_data["imagen"])
            avatar7.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form7= AvatarFormulario()
    return render (request, "AppCoder/agregarAvatar.html", {"formulario": form7})
'''

def about(request):
    return render(request, 'AppCoder/about.html')

def usuarios(request):
    usuarios= Avatar.objects.all()
    contextoUsuarios={'user': usuarios}
    return render(request, "AppCoder/usuarios.html",contextoUsuarios )


