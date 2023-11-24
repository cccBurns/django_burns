from django.db import models
from ckeditor.fields import RichTextField

class Monitor(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = RichTextField()
    anio = models.IntegerField()
    foto = models.ImageField(upload_to='foto', null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'