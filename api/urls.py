from django.urls import path, include
from .views import LivroViewSet, UsuarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('livros', LivroViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]