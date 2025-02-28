from rest_framework import serializers
from apps.banco_dados.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['matricula','nome','username','telefone','email']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nome','descricao']

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = ['id','nome','descricao','categoria','disponivel']