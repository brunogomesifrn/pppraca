from django.db import models

# Create your models here.
class Espaco(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField()