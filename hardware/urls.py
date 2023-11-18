from django.urls import path
from hardware.views import ListadoProcesadores, CrearProcesador, ActualizarProcesador, EliminarProcesador, DetalleProcesador

urlpatterns = [
    path('procesadores/', ListadoProcesadores.as_view(), name='procesadores'),
    path('procesadores/crear/', CrearProcesador.as_view(), name='crear_procesador'),
    path('procesadores/<int:pk>/', DetalleProcesador.as_view(), name='detalle_procesador'),
    path('procesadores/<int:pk>/actualizar/', ActualizarProcesador.as_view(), name='actualizar_procesador'),
    path('procesadores/<int:pk>/eliminar/', EliminarProcesador.as_view(), name='eliminar_procesador'),
]