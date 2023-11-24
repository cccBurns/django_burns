from django.urls import path
from hardware.views import ListadoProcesadores, CrearProcesador, ActualizarProcesador, EliminarProcesador, DetalleProcesador, ListadoPlacas, CrearPlaca, ActualizarPlaca, EliminarPlaca, DetallePlaca, productos

urlpatterns = [
    path('procesadores/', ListadoProcesadores.as_view(), name='procesadores'),
    path('procesadores/crear/', CrearProcesador.as_view(), name='crear_procesador'),
    path('procesadores/<int:pk>/', DetalleProcesador.as_view(), name='detalle_procesador'),
    path('procesadores/<int:pk>/actualizar/', ActualizarProcesador.as_view(), name='actualizar_procesador'),
    path('procesadores/<int:pk>/eliminar/', EliminarProcesador.as_view(), name='eliminar_procesador'),
    path('placas/', ListadoPlacas.as_view(), name='placas'),
    path('placas/crear/', CrearPlaca.as_view(), name='crear_placa'),
    path('placas/<int:pk>/', DetallePlaca.as_view(), name='detalle_placa'),
    path('placas/<int:pk>/actualizar/', ActualizarPlaca.as_view(), name='actualizar_placa'),
    path('placas/<int:pk>/eliminar/', EliminarPlaca.as_view(), name='eliminar_placa'),
    path('productos/', productos, name='productos'),
]