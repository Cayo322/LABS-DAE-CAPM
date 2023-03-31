from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
def index(request):
    context ={
        'titulo': "Formulario,"
    }
    return render(request, 'calculator.html', context)

@requires_csrf_token
def resultado(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operacion = request.POST['operacion']
        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        else:
            resultado = num1 * num2
        return render(request, 'resultado.html', {'resultado': resultado})
    else:
        return render(request, 'calculator.html')
