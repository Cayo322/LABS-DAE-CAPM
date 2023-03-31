from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from cmath import *
# Create your views here.
def index(request):
    context ={
        'titulo': "Formulario2,"
    }
    return render(request, 'form.html', context)

@requires_csrf_token
def resultado(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        val = num1/2
        resultado = (val**2)*pi*num2
        return render(request, 'resultado.html', {'resultado': resultado})

