from django.db import models

class Livro(models.Model):
    Titulo = models.CharField(max_length=30)
    Descricao = models.TextField(max_length=200)
    Autor = models.CharField(max_length=50)
    Data_lancamento = models.DateField()