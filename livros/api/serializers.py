from rest_framework import serializers
from livros import models

class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.livros
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.livros
        fields = '__all__'
