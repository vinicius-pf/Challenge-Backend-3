from django.contrib.auth.models import User
from django.test import TestCase
from orcamento.models import Receita, Despesa

class ReceitaModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('c3po', password = 'r2d2')

        self.receita = Receita(
            descricao = 'Receita do teste Automatizado',
            valor = 200,
            data = '2022-08-20',
            usuario = self.user
        )
    
    def test_verifica_informacoes_da_receita(self):
        """Teste que verifica as informações da receita com valores passados no setUp"""

        self.assertEqual(self.receita.descricao, 'Receita do teste Automatizado')
        self.assertEqual(self.receita.valor, 200)
        self.assertEqual(self.receita.data, '2022-08-20')
        self.assertEqual(self.receita.usuario, self.user)



class DespesaModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('c3po', password = 'r2d2')

        self.despesa = Despesa(
            descricao = 'Despesa do teste Automatizado',
            valor = 200,
            data = '2022-08-20',
            usuario = self.user
        )

    def test_verifica_informacoes_da_despesa(self):
        """Teste que verifica as informações da despesa com valores passados no setUp e valores default"""

        self.assertEqual(self.despesa.descricao, 'Despesa do teste Automatizado')
        self.assertEqual(self.despesa.valor, 200)
        self.assertEqual(self.despesa.data, '2022-08-20')
        self.assertEqual(self.despesa.usuario, self.user)
        self.assertEqual(self.despesa.categoria, 'O')
