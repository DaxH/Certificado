from django import forms
from documentos.models import *

class DateInput(forms.DateInput):
    """docstring forDateInput."""
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """docstring forTime."""
    input_type='time'

class DocumentoForm(forms.ModelForm):
    """DocumentoForm description)"""

    class Meta:
        model = Documento

        fields='__all__'

        labels={
            'usuario' : 'Participante'
        }
        widgets={
            'fecha_inicio':DateInput(),
            'hora':TimeInput(),
            'fecha_fin':DateInput(),
        }

class EntidadEmisoraForm(forms.ModelForm):
    """docstring for EntidadEmisoraForm."""
    class Meta:
        model = EntidadEmisora

        fields='__all__'
