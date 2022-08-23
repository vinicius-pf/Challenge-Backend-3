from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationUserReceitaTestCase(APITestCase):
    
    def setUp(self):
        self.list_url_receita = reverse('Receitas-list')
        self.list_url_despesa = reverse('Despesas-list')
        self.user = User.objects.create_user('c3po', password = 'r2d2')
    
    def test_autenticacao_de_um_user_com_credenciais_corretas(self):
        """Teste que verifica a authenticação de um user com as credenciais corretas."""

        user = authenticate(username= 'c3po', password='r2d2')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET não autorizada nas URIs de receita e despesa."""

        response_receita = self.client.get(self.list_url_receita)
        response_despesa = self.client.get(self.list_url_despesa)
        self.assertEqual(response_receita.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_despesa.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_de_user_com_username_incorreto(self):
        """Teste que verifica a autenticação de usuários com user_name incorreto."""

        user = authenticate(username= 'cp3o', password='r2d2')
        self.assertFalse((user is not None) and user.is_authenticated)
    
    def test_autenticacao_de_user_com_senha_incorreta(self):
        """Teste que verifica a autenticação de usuários com senha incorreta."""

        user = authenticate(username= 'c3po', password='r22d')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_user_autenticado(self):
        """Teste que verifica uma requisição GET de um user autenticado"""

        self.client.force_authenticate(self.user)
        response_receita = self.client.get(self.list_url_receita)
        response_despesa = self.client.get(self.list_url_despesa)
        self.assertEqual(response_receita.status_code, status.HTTP_200_OK)
        self.assertEqual(response_despesa.status_code, status.HTTP_200_OK)


