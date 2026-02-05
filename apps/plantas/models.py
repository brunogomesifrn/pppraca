from django.db import models
from apps.espacos.models import Espaco
# Create your models here.

class Familia(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    imagem = models.ImageField(upload_to="familias/")

    def __str__(self):
        return self.nome

class Planta(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT,related_name="plantas")
    nome_popular = models.CharField(max_length=255)
    nome_cientifico = models.CharField(max_length=255)
    origem = models.CharField(max_length=255)
    usos = models.CharField(max_length=255)
    saberes_afro = models.CharField(max_length=255)
    saberes_indigenas = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to="qrcodes/")
    id_espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_popular

class FotosPlanta(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="fotos")
    nome = models.CharField(max_length=255, blank=True)
    imagem_planta = models.ImageField(upload_to="plantas/fotos/")
    
    def __str__(self):
        return self.nome or f"Foto de {self.planta.nome_popular}"
