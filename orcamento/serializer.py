from rest_framework import serializers
from orcamento.models import Receita, Despesa

class ReceitaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receita
        fields = ['id', 'descricao', 'valor', 'data']


class DespesaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Despesa
        fields = ['id', 'descricao', 'valor', 'data']
