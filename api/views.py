from django.shortcuts import render
from .models import Livro, UsuarioPersonalizado
from .serializers import LivroSerializer, UsuarioSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser,)

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

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioSerializer