from django.shortcuts import render

def home_view(request):
    context = {
        'message': '¡Hola, mundo!'
    }
    return render(request, 'home.html', context=context)
