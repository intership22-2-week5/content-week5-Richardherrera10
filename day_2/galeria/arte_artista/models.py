from django.db import models
from email.mime import image
from turtle import title

# Create your models here.

class Arte(models.Model):
  tipo = models.CharField(max_length=50)
  nombre = models.CharField(max_length=100)
  fecha = models.DateTimeField()
  valor = models.FloatField()

  def __str__(self):
    return f'{self.tipo} - {self.fecha} - {self.valor}'


class Artista(models.Model):
  nombreCompleto = models.CharField(max_length=200)
  correo = models.CharField(max_length=200)
  edad = models.IntegerField()

  def __str__(self):
    return f'{self.nombreCompleto} - {self.correo} - {self.edad}'


class Arte_Artista(models.Model):
  arte = models.ForeignKey(Arte, on_delete=models.CASCADE)
  artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.arte} - {self.artista}'


class Multimedia(models.Model):
  tipo = models.CharField(max_length=50)
  uri = models.CharField(max_length=150)
  arte  = models.ForeignKey(Arte, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.id} - {self.arte.nombre} - {self.tipo} '


class Portafolio(models.Model):
  descripcion = models.CharField(max_length=250)
  multimedia = models.ForeignKey(Multimedia, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.descripcion} - {self.multimedia.tipo}'

class Exposicion(models.Model):
  fecha = models.DateTimeField()
  lugar = models.CharField(max_length=250)
  descripcion = models.CharField(max_length = 450)
  portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE)