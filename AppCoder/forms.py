from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar

class FormularioCurso(forms.Form):
    nombre = forms.CharField()
    #correo = forms.EmailField()
    #nombrecurso = forms.CharField()
    camada = forms.IntegerField()

class FormularioTurno(forms.Form):
    servicio= forms.CharField()
    nombre= forms.CharField()
    fechaTurno= forms.DateField()

class FormularioProductos(forms.Form):
    nombre=forms.CharField()
    marca=forms.CharField()

class FormularioRegistro(UserCreationForm):
    email= forms.EmailField(label= "Ingrese su correo ")
    #is_staff=forms.BooleanField(label= "Tilde si pertenece al staff")
    password1: forms.CharField(label= "Ingrese una contraseña ", widget=forms.PasswordInput)
    password2: forms.CharField(label= "Repita la contraseña ",widget=forms.PasswordInput)
    first_name: forms.CharField(label= "Ingrese su nombre")
    last_name: forms.CharField(label= "Ingrese su apellido")


    class Meta:
        model= User
        fields= ["username","email","password1", "password2","first_name", "last_name"]

class FormularioEditarUsuario(UserCreationForm):
    email= forms.EmailField(label= "Ingrese su correo ")
    password1: forms.CharField(label= "Ingrese una contraseña ", widget=forms.PasswordInput)
    password2: forms.CharField(label= "Repita la contraseña ",widget=forms.PasswordInput)
    first_name: forms.CharField(label= "Ingrese su nombre")
    last_name: forms.CharField(label= "Ingrese su apellido")


    class Meta:
        model= User
        fields= ["email","password1", "password2","first_name", "last_name"]

class AvatarFormulario(forms.ModelForm):
    model = Avatar
    class Meta:
        fields= ["user", "imagen"]
