from django.urls import path
from inicio.views import inicio, about, contacto, productos

urlpatterns = [
    path('', inicio, name='inicio'),    
    path('about/', about, name='about'),
    path('contacto/', contacto, name='contacto'),
    path('productos/', productos, name='productos'),
]