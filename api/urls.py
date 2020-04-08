from django.urls import path, include
from .views import LivroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('livros/', LivroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]