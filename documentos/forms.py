from django import forms
from documentos.models import Documento


class DocumentoForm(forms.ModelForm):
    """DocumentoForm description)"""
    class Meta:
        model = Documento

        fields='__all__'

        labels={
            'usuario' : 'Participante'
        }
