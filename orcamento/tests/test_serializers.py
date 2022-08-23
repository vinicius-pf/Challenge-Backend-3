from django.test import TestCase
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer
from django.contrib.auth.models import User

class ReceitaSerializerTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('c3po', password = 'r2d2')

        self.receita = Receita(
            descricao = 'Receita do teste Automatizado',
            valor = 200.00,
            data = '2022-08-20',
            usuario = self.user
        )
        self.serializer = ReceitaSerializer(instance = self.receita)

    def test_verifica_campos_serializados_receita(self):
        """Teste que verifica se os campos estão sendo serializados corretamente"""

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'descricao', 'valor', 'data']))

    def test_verifica_conteudo_dos_campos_serializados_receita(self):
        """Teste que verifica o conteúdo dos campos serializados de receita"""

        data = self.serializer.data
        self.assertEqual(data['descricao'], self.receita.descricao)
        self.assertEqual(data['data'], self.receita.data)
        self.assertAlmostEqual(float(data['valor']), self.receita.valor, places = 2)

class DespesaSerializerTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('c3po', password = 'r2d2')

        self.despesa = Despesa(
            descricao = 'Despesa do teste Automatizado',
            valor = 200.00,
            data = '2022-08-20',
            usuario = self.user,
            categoria = 'I'
        )
        self.serializer = DespesaSerializer(instance = self.despesa)

    def test_verifica_campos_serializados_despesa(self):
        """Teste que verifica se os campos estão sendo serializados corretamente"""

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'descricao', 'data', 'valor', 'categoria']))

    def test_verifica_conteudo_dos_campos_serializados_despesa(self):
        """Teste que verifica o conteúdo dos campos serializados das despesas"""

        data = self.serializer.data
        self.assertEqual(data['descricao'], self.despesa.descricao)
        self.assertEqual(data['data'], self.despesa.data)
        self.assertAlmostEqual(float(data['valor']), self.despesa.valor, places = 2)
        self.assertEqual(data['categoria'], 'Imprevistos')