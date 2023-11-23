from django.urls import path
from inicio.views import inicio, monitores, crear_monitor, eliminar_monitor, actualizar_monitor, detalle_monitor, about

urlpatterns = [
    path('', inicio, name='inicio'),
    path('monitores/', monitores, name='monitores'),
    path('monitores/crear/', crear_monitor, name='crear_monitor'),
    path('monitores/<int:monitor_id>/', detalle_monitor, name='detalle_monitor'),
    path('monitores/<int:monitor_id>/eliminar/', eliminar_monitor, name='eliminar_monitor'),
    path('monitores/<int:monitor_id>/actualizar/', actualizar_monitor, name='actualizar_monitor'),
    path('about/', about, name='about'),
]