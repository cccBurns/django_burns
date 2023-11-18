from django import forms
from inicio.models import Monitor
from ckeditor.fields import RichTextFormField


# otrea version de formulario de paleta
# class PaletaFormulario(forms.Form):
#     class Meta:
#         model = Paleta
#         fields = ['marca', 'descripcion', 'anio']
        

class BaseMonitorFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()
    

class CrearMonitorFormulario(BaseMonitorFormulario):
    ...


class ActualizarMonitorFormulario(BaseMonitorFormulario):
    ...
    
class BusquedaMonitorFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    