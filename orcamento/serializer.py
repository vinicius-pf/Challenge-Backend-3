from rest_framework import serializers
from orcamento.models import Receita, Despesa
from django.contrib.auth.models import User

class ReceitaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receita
        fields = ['id', 'descricao', 'data', 'valor']


class DespesaSerializer(serializers.ModelSerializer):
    
    categoria = serializers.SerializerMethodField()

    class Meta:
        model = Despesa
        fields = ['id', 'descricao', 'data', 'valor', 'categoria']

    def get_categoria(self, obj):
        return obj.get_categoria_display()