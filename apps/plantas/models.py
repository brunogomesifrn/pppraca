from django.db import models
from apps.espacos.models import Espaco
# Create your models here.

class Familia(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to="familias/")

    def __str__(self):
        return self.nome

class Planta(models.Model):
    nome_popular = models.CharField(max_length=255)
    nome_cientifico = models.CharField(max_length=255)
    origem = models.CharField(max_length=255)
    usos = models.CharField(max_length=255)
    saberes_afro = models.CharField(max_length=255)
    saberes_indigenas = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to="qrcodes/")
    # id_espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    # id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    id_espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE, null=True, blank=True)
    id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_popular

class FotosPlanta(models.Model):
    nome = models.CharField(max_length=255)
    id_planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
