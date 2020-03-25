from django.shortcuts import render,redirect

from documentos.models import Documento, EntidadEmisora
from documentos.forms import DocumentoForm, EntidadEmisoraForm

from usuarios.models import Usuario
from usuarios.forms import UsuarioForm


def validar_credenciales(request):

    return render(request, 'documentos/credenciales.html')

def mostrar_certificado(request):
    '''Si las credenciales existen muestra el certificado que corresponde'''

    #valores ingresados desde el template documentos/validar_credenciales.html
    input_cedula = request.POST.get('buscar_cedula')
    input_codigo_certificado = request.POST.get('buscar_codigo')

    mensaje_error = False
    #validamos
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
    '''Funcion para crear un proyecto '''
    documento_form = DocumentoForm()
    if request.method == 'POST':

        documento_form = DocumentoForm(request.POST)
        # validamos
        if documento_form.is_valid():

            documento_form.save()

            return redirect('documentos:certificado_list')

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
    '''Lista todos los Proyectos'''
    documentos = Documento.objects.all().order_by('-fecha_inicio')

    context={
            'documentos':documentos,
    }

    return render(request, 'documentos/certificado_list.html', context)

def documento_edit(request, documento_pk):

    documento = Documento.objects.get(pk = documento_pk)
    documento_form = DocumentoForm(instance = documento)
    fecha_inicio =  documento.fecha_inicio
    fecha_fin = documento.fecha_fin
    if request.method == 'POST':
        documento_form = DocumentoForm(request.POST, instance = documento)

        if documento_form.is_valid():
            documento_form.save()

            return redirect ('documentos:certificado_list')
        else:
            print('ERROR FORM DOCUEMTNO ', documento_form.errors)

            context={
                    'fecha_inicio':fecha_inicio,
                    'fecha_fin':fecha_fin,
                    'documento_pk':documento_pk,
                    'documento_form':documento_form,
            }

            return render (request, 'documentos/certificado_edit.html', context)

    context={
            'fecha_inicio':fecha_inicio,
            'fecha_fin':fecha_fin,
            'documento_pk':documento_pk,
            'documento_form':documento_form,
    }
    return render (request, 'documentos/certificado_edit.html', context)

def documento_detail(request, documento_pk):

    documento = Documento.objects.get(pk = documento_pk)

    context = {
                'documento':documento
    }
    return render(request, 'documentos/certificado_detail.html', context)

def entidad_create(request, documento_pk):

    entidad_form = EntidadEmisoraForm()

    if request.method == 'POST':
        entidad_form = EntidadEmisoraForm(request.POST, request.FILES)

        if entidad_form.is_valid():

            entidad_form.save()

        else:
            context={
                    'entidad_form':entidad_form,
                    'documento_pk':documento_pk
            }
            return render(request, 'documentos/entidad_create.html', context)

    context={
            'entidad_form':entidad_form,
            'documento_pk':documento_pk

    }
    return render(request, 'documentos/entidad_create.html', context)


def entidad_list(request):

    entidades = EntidadEmisora.objects.all()

    context={
            'entidades':entidades,
    }

    return render(request, 'documentos/entidad_list.html', context)

def entidad_detail(request, entidad_pk):

    entidad = EntidadEmisora.objects.get(pk = entidad_pk)

    context={
            'entidad':entidad
    }

    return render(request, 'documentos/entidad_detail.html', context)

def entidad_edit(request, entidad_pk):

    entidad = EntidadEmisora.objects.get(pk = entidad_pk)
    entidad_form = EntidadEmisoraForm(instance = entidad)

    if request.method == "POST":
        entidad_form = EntidadEmisoraForm(request.POST, request.FILES, instance = entidad)

        if entidad_form.is_valid():
            entidad_form.save()

        else:

            context={
                    'entidad_form':entidad_form,
            }

            return render(request, 'documentos/entidad_edit.html', context)

    context={
            'entidad_form':entidad_form,
    }

    return render(request, 'documentos/entidad_edit.html', context)
