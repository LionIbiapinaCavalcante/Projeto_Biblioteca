from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.email

# class Pessoa(models.Model):
#     nome = models.CharField(max_lenght=35)
#     cpf = models.CharField(max_lenght=11)
#     idade = models.IntegerField()
#     rua = models.CharField(max_lenght=60)
#     bairro = models.CharField(max_lenght=60)
#     numero = models.IntegerField()

