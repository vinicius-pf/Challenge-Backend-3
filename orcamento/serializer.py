from rest_framework import serializers
from orcamento.models import Receita, Despesa
from django.contrib.auth.models import User

class ReceitaSerializer(serializers.ModelSerializer):
    
    usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Receita
        exclude = []


class DespesaSerializer(serializers.ModelSerializer):
    
    usuario = serializers.ReadOnlyField(source='usuario.username')
    categoria = serializers.SerializerMethodField()

    class Meta:
        model = Despesa
        exclude = []

    def get_categoria(self, obj):
        return obj.get_categoria_display()

class UsuarioSerializer(serializers.ModelSerializer):

    receitas = serializers.PrimaryKeyRelatedField(many=True, queryset=Receita.objects.all())
    despesas = serializers.PrimaryKeyRelatedField(many=True, queryset=Despesa.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'receitas', 'despesas']