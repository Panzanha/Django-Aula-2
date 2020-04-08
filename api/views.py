from django.shortcuts import render
from .models import Livro
from .serializers import LivroSerializer
from rest_framework import viewsets

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

