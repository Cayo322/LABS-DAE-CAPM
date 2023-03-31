from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.
def index(request):
    context ={
        'titulo': "Formulario,"
    }
    return render(request, 'formulario.html', context)
@requires_csrf_token
def enviar(request):
    context={
        'Titulo': "Respuesta",
        'nombre':request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'respuesta.html',context)

        