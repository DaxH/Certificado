from django.shortcuts import render,redirect

from documentos.models import Documento, EntidadEmisora
from documentos.forms import DocumentoForm

from usuarios.models import Usuario

def validar_credenciales(request):

    return render(request, 'documentos/credenciales.html')

def mostrar_certificado(request):

    input_cedula = request.POST.get('buscar_cedula')
    input_codigo_certificado = request.POST.get('buscar_codigo')
    mensaje_error = False

    if input_cedula and input_codigo_certificado:
        try:
            usuario = Usuario.objects.get(cedula = input_cedula)
            certificado = Documento.objects.get(usuario = usuario, codigo = input_codigo_certificado)
            entidad_emisora =  EntidadEmisora.objects.filter(documento = certificado.pk)

            context = {
                    'input_cedula':input_cedula,
                    'input_codigo_certificado':input_codigo_certificado,
                    'usuario':usuario,
                    'entidad_emisora':entidad_emisora,
                    'certificado':certificado,
            }

            return render(request, 'documentos/certificado.html', context)

        except Usuario.DoesNotExist:

            mensaje_error = True
            context = {
                    'mensaje_error':mensaje_error
            }

        except Documento.DoesNotExist:

            mensaje_error = True
            context = {
                    'mensaje_error':mensaje_error
            }

    else:
        return render(request, 'documentos/certificado.html')

    return render(request, 'documentos/certificado.html', context)

def documento_create(request):

    documento_form = DocumentoForm()
    if request.method == 'POST':

        documento_form = DocumentoForm(request.POST)

        if documento_form.is_valid():

            documento_form.save()

            return redirect('documentos:credenciales')

        else:

            print('ERROR FORM DOCUMENTO ', documento_form.errors)

            context={
                    'documento_form':documento_form
            }
            return render(request, 'documentos/documento_create.html', context)

    context={
            'documento_form':documento_form
    }
    return render(request, 'documentos/documento_create.html', context)


def documento_list(request):

    documentos = Documento.objects.all().order_by('fecha_inicio')

    context={
            'documentos':documentos,
    }

    return render(request, 'documentos/certificado_list.html', context)
