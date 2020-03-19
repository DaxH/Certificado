from django.shortcuts import render,redirect
from usuarios.forms import UsuarioForm

# Create your views here.

def usuario_create(request):

    usuario_form = UsuarioForm()

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)

        if usuario_form.is_valid():

            usuario_form.save()

            return redirect('documentos:certificado_create')

        else:
            print('ERROR FORM USUARIO ', usuario_form.errors)

            context={
                'usuario_form':usuario_form,
            }
            return render(request, 'usuarios/usuario_create.html', context)

    context={
        'usuario_form':usuario_form,
    }

    return render(request, 'usuarios/usuario_create.html', context)
