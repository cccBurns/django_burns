from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Monitor
from inicio.forms import CrearMonitorFormulario, BusquedaMonitorFormulario, ActualizarMonitorFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    
    # v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # v3
    return render(request, 'inicio/inicio.html', {})

def monitores(request):
    
    # v1
    # marca_a_buscar = request.GET.get('marca')
    
    # if marca_a_buscar:
    #     listado_de_paletas = Paleta.objects.filter(marca__icontains=marca_a_buscar)
    # else:
    #     listado_de_paletas = Paleta.objects.all()
    
    # v2
    formulario = BusquedaMonitorFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_monitores = Monitor.objects.filter(marca__icontains=marca_a_buscar)
    
    formulario = BusquedaMonitorFormulario()
    return render(request, 'inicio/monitores.html', {'formulario': formulario, 'listado_de_monitores': listado_de_monitores})

@login_required
def crear_monitor(request):
    
    # v1 (HTML)
    # # print('==============')
    # # print('GET')
    # # print(request.GET)
    # # print('==============')
    # # print('POST')
    # # print(request.POST)
    
    # if request.method == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
        
    #     paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
    #     paleta.save()
    
    # v2 (Django Forms)
    if request.method == 'POST':
        formulario = CrearMonitorFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
    
            monitor = Monitor(marca=marca.lower(), descripcion=descripcion, anio=anio)
            monitor.save()
            
            return redirect('monitores')
        else:
            return render(request, 'inicio/crear_monitor.html', {'formulario': formulario})
        
    formulario = CrearMonitorFormulario()
    return render(request, 'inicio/crear_monitor.html', {'formulario': formulario})

@login_required
def eliminar_monitor(request, monitor_id):
    monitor_a_eliminar = Monitor.objects.get(id=monitor_id)
    monitor_a_eliminar.delete()
    return redirect("monitores")

@login_required
def actualizar_monitor(request, monitor_id):
    monitor_a_actualizar = Monitor.objects.get(id=monitor_id)
    
    if request.method == "POST":
        formulario = ActualizarMonitorFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            monitor_a_actualizar.marca = info_nueva.get('marca')
            monitor_a_actualizar.descripcion = info_nueva.get('descripcion')
            monitor_a_actualizar.anio = info_nueva.get('anio')
            
            monitor_a_actualizar.save()
            return redirect('monitores')
        else:
            return render(request, 'inicio/actualizar_monitor.html', {'formaulario': formulario})
    
    
    formulario = ActualizarMonitorFormulario(initial={'marca': monitor_a_actualizar.marca, 'descripcion': monitor_a_actualizar.descripcion,'anio': monitor_a_actualizar.anio})
    return render(request, 'inicio/actualizar_monitor.html', {'formulario': formulario})

def detalle_monitor(request, monitor_id):
    monitor = Monitor.objects.get(id=monitor_id)
    return render(request, 'inicio/detalle_monitor.html', {'monitor': monitor})