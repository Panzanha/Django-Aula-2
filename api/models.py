from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    Titulo = models.CharField(max_length=30)
    Descricao = models.TextField(max_length=200)
    Autor = models.CharField(max_length=50)
    preco = models.FloatField()

class UsuarioPersonalizado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=10)
    CPF = models.CharField(max_length=10)
