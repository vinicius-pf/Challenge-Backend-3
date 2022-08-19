from rest_framework import viewsets, filters, generics
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer, UsuarioSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db.models import Sum
from django.contrib.auth.models import User


class ReceitasViewSet(viewsets.ModelViewSet):
    """Listando todas as receitas"""

    def get_queryset(self):
        queryset = Receita.objects.filter(usuario=self.request.user)
        return queryset

    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class DespesasViewSet(viewsets.ModelViewSet):
    """Listando todas as receitas"""

    def get_queryset(self):
        queryset = Despesa.objects.filter(usuario=self.request.user)
        return queryset
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ListaReceitasMesViewSet(viewsets.ModelViewSet):
    """Listando as receitas por ano e mês"""

    serializer_class = ReceitaSerializer

    def get_queryset(self):
        ano = self.kwargs['year']
        mes = self.kwargs['month']
        return Receita.objects.filter(data__year=ano, data__month=mes, usuario=self.request.user)

class ListaDespesasMesViewSet(viewsets.ModelViewSet):
    """Listando as despesas por ano e mês"""

    serializer_class = DespesaSerializer

    def get_queryset(self):
        ano = self.kwargs['year']
        mes = self.kwargs['month']
        return Despesa.objects.filter(data__year=ano, data__month=mes, usuario=self.request.user)

class ResumoAnoMesViewSet(viewsets.ViewSet):
    """Listando um resumo de receitas e despesas por ano e mês."""

    queryset = Receita.objects.none()

    def list(self, request, ano, mes):
        soma_receitas = Receita.objects.filter(data__year=ano, data__month=mes, usuario=self.request.user).aggregate(Sum('valor')) ['valor__sum'] or 0
        soma_despesas = Despesa.objects.filter(data__year=ano, data__month=mes, usuario=self.request.user).aggregate(Sum('valor')) ['valor__sum'] or 0
        despesa_por_categoria = Despesa.objects.filter(data__year=ano, data__month=mes, usuario=self.request.user).values('categoria').annotate(Total = Sum('valor'))
        saldo = soma_receitas - soma_despesas

        return Response({
            'Valor recebido': soma_receitas,
            'Valor gasto': soma_despesas,
            'Saldo do mês': saldo,
            'Despesa por categoria': despesa_por_categoria
        })

class UsuarioViewSet(generics.ListAPIView):
    """"Lista todos os usuários do sistema"""
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer