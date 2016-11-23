from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField


class Perfil(models.Model):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('S', 'Sin especificar'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    genero = models.CharField("género", max_length=1, choices=GENERO_CHOICES, blank=True, default='S')
    fecha_nacimiento = models.DateField("fecha de nacimiento", null=True, blank=True)
    direccion = models.CharField("dirección", max_length=150, null=True, blank=True)
    foto = ThumbnailerImageField(
        upload_to="perfil_usuario",
        null=True,
        blank=True,
        editable=True,)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


User.perfil = property(lambda u: Perfil.objects.get_or_create(user=u)[0])
