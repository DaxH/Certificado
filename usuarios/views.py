from django.shortcuts import render,redirect

from documentos.models import Documento

from usuarios.models import *
from usuarios.forms import *

# Create your views here.

def usuario_create(request, documento_pk):
    '''Crea un Usuario '''
    usuario_form = UsuarioForm()
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)

        if usuario_form.is_valid():

            usuario_form.save()

        else:
            print('ERROR FORM USUARIO ', usuario_form.errors)

            context={
                'documento_pk':documento_pk,
                'usuario_form':usuario_form,
            }
            return render(request, 'usuarios/usuario_create.html', context)

    context={
        'documento_pk':documento_pk,
        'usuario_form':usuario_form,
    }

    return render(request, 'usuarios/usuario_create.html', context)

def usuario_list(request):

    '''Lista Todos los Usuarios'''

    usuarios = Usuario.objects.all()

    context={
            'usuarios':usuarios,
    }

    return render(request, 'usuarios/usuario_list.html', context)


def usuario_edit(request, usuario_pk):

    usuario = Usuario.objects.get(pk = usuario_pk)
    usuario_form = UsuarioForm(instance = usuario)

    if request.method == 'POST':

        usuario_form = UsuarioForm(request.POST, instance = usuario)

        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('usuarios:usuario_list')
        else:
            context={
                    'usuario_form':usuario_form,
            }
            return render(request, 'usuarios/usuario_edit.html', context)

    context={
            'usuario_form':usuario_form,
    }
    return render(request, 'usuarios/usuario_edit.html', context)

def usuario_detail(request, usuario_pk):

    usuario = Usuario.objects.get(pk = usuario_pk)
    proyectos = Documento.objects.filter(usuario = usuario)

    context={
            'usuario':usuario,
            'proyectos':proyectos
    }

    return render(request, 'usuarios/usuario_detail.html', context)
