from django.shortcuts import render

def operaciones(request, num1, num2):
    resultado_suma = int(num1) + int(num2)
    resultado_resta = int(num1) - int(num2)
    resultado_multiplicacion = int(num1) * int(num2)
    
    context = {
        'num1': num1,
        'num2': num2,
        'resultado_suma': resultado_suma,
        'resultado_resta': resultado_resta,
        'resultado_multiplicacion': resultado_multiplicacion,
    }
    
    return render(request, 'operaciones/operaciones.html', context)