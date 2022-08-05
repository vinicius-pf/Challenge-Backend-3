from rest_framework import viewsets
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ReceitasViewSet(viewsets.ModelViewSet):
    """Listando todas as receitas"""
    
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DespesasViewSet(viewsets.ModelViewSet):
    """Listando todas as receitas"""

    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]