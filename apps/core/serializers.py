from rest_framework import serializers
from apps.banco_dados.models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']