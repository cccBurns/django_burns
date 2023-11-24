from django.shortcuts import render


def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def about(request):
    
    return render(request, 'inicio/about.html', {})

def productos(request):
    
    return render(request, 'inicio/productos.html', {})

def contacto(request):
    
    return render(request, 'inicio/contacto.html', {})

