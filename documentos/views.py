from django.shortcuts import render,redirect

from documentos.models import Documento
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
            certificado_imprimir = Documento.objects.get(usuario = usuario, codigo = input_codigo_certificado)
            print('USUARIO ', usuario)
            print('CERTIFICADO ', certificado_imprimir)

            context = {
                    'input_cedula':input_cedula,
                    'input_codigo_certificado':input_codigo_certificado,
                    'usuario':usuario,
                    'certificado_imprimir':certificado_imprimir,
            }

        except Usuario.DoesNotExist and Documento.DoesNotExist:


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
