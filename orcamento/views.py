from rest_framework import viewsets, filters 
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg

class ReceitasViewSet(viewsets.ModelViewSet):
    """Listando todas as receitas"""
    
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']

class DespesasViewSet(viewsets.ModelViewSet):
    """Listando todas as receitas"""

    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']

class ListaReceitasMesViewSet(viewsets.ModelViewSet):
    """Listando as receitas por ano e mês"""

    serializer_class = ReceitaSerializer

    def get_queryset(self):
        ano = self.kwargs['year']
        mes = self.kwargs['month']
        return Receita.objects.filter(data__year=ano, data__month=mes)

class ListaDespesasMesViewSet(viewsets.ModelViewSet):
    """Listando as despesas por ano e mês"""

    serializer_class = DespesaSerializer

    def get_queryset(self):
        ano = self.kwargs['year']
        mes = self.kwargs['month']
        return Despesa.objects.filter(data__year=ano, data__month=mes)

class ResumoAnoMesViewset(viewsets.ModelViewSet):
    """Listando um resumo de receitas e despesas por ano e mês."""

    receitas = Receita.objects.aggregate(Avg('valor'))
    despesas = Despesa.objects.all()

    def get_queryset(self):
        return self.receitas