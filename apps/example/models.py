from django.db import models
from django.urls import reverse_lazy
from django.conf import settings

class BaseName(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombre')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Profiles(BaseName):
    username = models.CharField(max_length=150, verbose_name='Nombre')
    age = models.IntegerField(verbose_name='Edad')

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'

