from rest_framework import serializers
from .models import Livro, UsuarioPersonalizado 

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'Titulo', 'Descricao', 'Autor', 'preco']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['id', 'telefone', 'CPF']
