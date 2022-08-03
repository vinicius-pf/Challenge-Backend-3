from rest_framework import viewsets
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer

class ReceitasViewSet(viewsets.ModelViewSet):
    """Listando todos as receitas do usuário."""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class DespesasViewSet(viewsets.ModelViewSet):
    """Listando todos as receitas do usuário."""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer