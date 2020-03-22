from django.shortcuts import render,redirect
from usuarios.forms import UsuarioForm

# Create your views here.

def usuario_create(request, documento_pk):

    usuario_form = UsuarioForm()
    print(documento_pk)
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
