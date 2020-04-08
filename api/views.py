from django.shortcuts import render
from .models import Livro
from .serializers import LivroSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    @action(detail=True, methods=['POST'])
    def set_preco(self, request, pk=None):
        if 'preco' in request.data:
            livro = Livro.objects.get(id=pk)
            preco = request.data['preco']
                        
            livro.preco = preco
            livro.save()
            response = {'message': 'Preco atualizado'}             
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'Voce precisa dar o preco'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
