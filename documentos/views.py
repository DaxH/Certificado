from django.shortcuts import render,redirect
from documentos.models import Documento, Entidad
from usuarios.models import Usuario

def validar_documento(request):
    documento = Documento.objects.all()

    context = {
        'documento':documento,
    }
    return render(request, 'validar_datos.html',context )

def mostrar_certificado(request):

    input_cedula = request.POST.get('buscar_cedula')
    input_codigo_certificado = request.POST.get('buscar_codigo')
    mensaje_error = False

    if input_cedula and input_codigo_certificado:
        try:
            usuario = Usuario.objects.get(cedula = input_cedula)
            certificado = Documento.objects.get(usuario = usuario, codigo = input_codigo_certificado)
            entidad_receptora = Entidad.objects.get(documento = certificado.pk, tipo = '1')
            entidad_emisora =  Entidad.objects.get(documento = certificado.pk, tipo = '2')

            context = {
                    'input_cedula':input_cedula,
                    'input_codigo_certificado':input_codigo_certificado,
                    'usuario':usuario,
                    'entidad_receptora':entidad_receptora,
                    'entidad_emisora':entidad_emisora,
                    'certificado':certificado,
            }

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

        context={
                'input_cedula':input_cedula,
                'input_codigo_certificado':input_codigo_certificado,
                }

    return render(request,'certificado.html', context)
