from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    """(UsuarioForm description)"""

    class Meta:
        model=Usuario

        fields='__all__'

        labels={
                'cedula':'Cédula',
                'nombre':'Nombe(s)',
                'apellido':'Apellido(s)',
                'telefono':'Télefono'
        }
        widgets={
                'telefono':forms.NumberInput(),
                'cedula':forms.NumberInput()
        }
