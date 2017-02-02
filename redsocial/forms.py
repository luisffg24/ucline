from django import forms

from redsocial.models import Area_Conocimiento


class Area_Conocimiento_form(forms.ModelFrom):

    class Meta:
        model = Area_Conocimiento

        fields = [
        	'nombre', 
        	'descripcion',
        ]
        labels = {
        	'nombre' : 'Nombre',
        	'descripcion' : 'Descripcion',
        }
        widgets = {
        	'nombre' : forms.TextImput(),
        	'descripcion' : forms.TextImput(),
        }
