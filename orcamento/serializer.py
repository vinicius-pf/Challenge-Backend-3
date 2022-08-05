from rest_framework import serializers
from orcamento.models import Receita, Despesa

class ReceitaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receita
        exclude = []


class DespesaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Despesa
        exclude = []
