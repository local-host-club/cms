from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

class Perfil(models.Model):
	GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('S', 'Sin especificar'),)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True, default='S')
	fecha_nacimiento = models.DateField(null=True, blank=True)
	direccion = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfils"

    def __str__(self):
        pass
    
