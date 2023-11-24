from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from hardware.models import Procesador, Placa
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def productos(request):
    
    return render(request, 'hardware/productos.html', {})

class ListadoProcesadores(ListView):
    model = Procesador
    context_object_name = 'listado_de_procesadores'
    template_name = 'hardware/procesadores.html'
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            listado_de_procesadores = self.model.objects.filter(marca__icontains=marca)
        else:
            listado_de_procesadores = self.model.objects.all()
        return listado_de_procesadores    
    
class CrearProcesador(LoginRequiredMixin, CreateView):
    model = Procesador
    template_name = "hardware/crear_procesador.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('procesadores')


class ActualizarProcesador(LoginRequiredMixin, UpdateView):
    model = Procesador
    template_name = "hardware/actualizar_procesador.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('procesadores')


class DetalleProcesador(DetailView):
    model = Procesador
    template_name = "hardware/detalle_procesador.html"


class EliminarProcesador(LoginRequiredMixin, DeleteView):
    model = Procesador
    template_name = "hardware/eliminar_procesador.html"
    success_url = reverse_lazy('procesadores')
    
    
    # PLACAS DE VIDEO  
    
class ListadoPlacas(ListView):
    model = Placa
    context_object_name = 'listado_de_placas'
    template_name = 'hardware/placas.html'
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            listado_de_placas = self.model.objects.filter(marca__icontains=marca)
        else:
            listado_de_placas = self.model.objects.all()
        return listado_de_placas   
    
class CrearPlaca(LoginRequiredMixin, CreateView):
    model = Placa
    template_name = "hardware/crear_placa.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('placas')


class ActualizarPlaca(LoginRequiredMixin, UpdateView):
    model = Placa
    template_name = "hardware/actualizar_placa.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('placas')


class DetallePlaca(DetailView):
    model = Placa
    template_name = "hardware/detalle_placa.html"


class EliminarPlaca(LoginRequiredMixin, DeleteView):
    model = Placa
    template_name = "hardware/eliminar_placa.html"
    success_url = reverse_lazy('Placas')