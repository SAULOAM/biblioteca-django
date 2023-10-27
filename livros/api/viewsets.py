from rest_framework import viewsets
from rest_framework import generics
from livros.api import serializers
from livros import models

class LivrosViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializers
    queryset = models.livros.objects.all()

class BookDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.livros.objects.all()
