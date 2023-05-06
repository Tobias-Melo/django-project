from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    senha = models.CharField(max_length=16)

    def __str__(self):
        return self.nome + " " + self.sobrenome