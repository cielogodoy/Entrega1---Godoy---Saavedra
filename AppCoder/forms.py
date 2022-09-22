from django import forms

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
