from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.email
