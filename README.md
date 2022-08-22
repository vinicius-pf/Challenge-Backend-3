# Alura Challenge Back-End 4ª Edição

Neste Repositório estão os meus projetos desenvolvidos no mês de Agosto 2022 como parte da quarta edição do [Alura Challenge Back-End](https://www.alura.com.br/challenges/back-end-4/). 

* [Sobre o Challenge](#sobre-o-challenge)
* [Desenvolvimento do Projeto](#desenvolvimento-do-projeto)
  + [Criação da API](#criação-da-api)
* [Entre em Contato](#entre-em-contato)

## Sobre o Challenge

Após alguns testes com protótipos feitos pelo time de UX de uma empresa, foi requisitada a primeira versão de uma aplicação para controle de orçamento familiar. A aplicação deve permitir que uma pessoa cadastre suas receitas e despesas do mês, bem como gerar um relatório mensal. Com o intuito de persistência de dados, será criado um banco de dados com as informações de despesas e receitas. Para pesquisa de informações no banco de dados e envio e recebimento de requerimentos, será desenvolvida uma API REST. 

## Desenvolvimento do Projeto

### Criação da API

No início do projeto, a empresa enviou alguns pedidos por meio de cards do [Trello](https://trello.com/b/B938DjhW/challenge-backend-semana-1). Esses pedidos incluiam algumas regras de negócio e qual o comportamento esperado da API.

De acordo com as regras de negócio, era necessário a criação de duas tabelas, uma para armazenar as receitas e outra para armazenar as despesas do usuário. Cada tabela devia conter as seguintes informações:

Coluna | Descrição
-------|----------
id | Identificador único da transação.
descrição | Descrição da transação, não podendo receber duas descrições iguais para o mesmo mês.
valor | Valor final da transação.
data | Data da transação.

Como requisitado, as tabelas foram armazenadas em um banco de dados. Neste projeto foi utilizado o [PostgreSQL](https://www.postgresql.org/) para armazenamento das informações.

Para a criação da API REST, foi utilizada a ferramenta [Django REST Framework](https://www.django-rest-framework.org/). Ele é baseado no framework [Django](https://www.djangoproject.com/) e utiliza a linguagem [Python](https://www.python.org/). Seguindo as boas práticas de programação, foi criada um *virtual enviroment*, ou `venv`. Nessa `venv` foram instalados os módulos que serão utilizados ao longo da aplicação. Além das bibliotecas já citadas, foi instalado também o módulo [Psycopg2](https://pypi.org/project/psycopg2/), para configurar e fazer a conexão com o banco de dados.

Após a criação do ambiente virtual, foi criada a aplicação que servirá de base para a API. Primeiramente os modelos para as transações foram criados e registrados dentro do arquivo `admin.py`. Além de criar o modelo para exibição e tranferência de informações, essa etapa também gera as tabelas no banco de dados. Apesar das duas transações possuírem as mesmas informações, foram criadas duas tabelas distintas na aplicação. Isso pode mudar de acordo com o desejo da empresa e com outros pedidos para o funcionamento da API.

```python
  class Receita(models.Model):
      descricao = models.CharField(max_length=200, unique_for_month='data')
      valor = models.DecimalField(max_digits = 10, decimal_places=2)
      data = models.DateField()

      def __str__(self):
          return self.descricao
```

Com o registro no arquivo de administração, foi possível efetuar testes de inclusão, edição e exclusão de registros no banco de dados por meio de um formulário web gerado pelo Django. Para que essas informações fossem visualizadas em formato JSON e as ações pudessem ser efetuadas por meio de requisições HTTP, uma API REST foi desenvolvida.

Como requisito da empresa, essa API deveria receber requisições do tipo GET, POST, PUT e DELETE em URIs específicas para receitas e despesas. Para testar a aplicação, foi utilizado a plataforma [Postman](https://www.postman.com/company/about-postman/). 

Primeiramente foi testada a requisição GET para as URIs `/receitas/` e `/despesas/`. Ambas as URIs receberam as informações desejadas com sucesso. Abaixo segue a resposta recebida pelo Postman em uma requisição GET para a URI `/despesas`.

![image](https://user-images.githubusercontent.com/6025360/183134349-feb2da10-e86b-4407-9894-744c15d2a4be.png)

Após isso, foi criada uma requisição do tipo POST nas mesmas URIs, com o intuito de verificar a resposta recebida pela plataforma de testes. Novamente o teste foi concluido com sucesso.

![image](https://user-images.githubusercontent.com/6025360/183134905-8b08fb5b-6a0b-4ca4-931b-e12f08512a23.png)

Nessa imagem percebe-se que mesmo incluindo a informação de `id`, esta não é considerada na criação do registro. Um dos requisitos da empresa é que a descrição da receita deve ser única dentro de um mesmo mês. Foi criado então um registro que deveria ser recusado para entender o comportamento do sistema.

![image](https://user-images.githubusercontent.com/6025360/183135267-8430fe37-c4ab-4966-a0f6-837d05e634c8.png)

Ao tentar incluir uma informação duplicada, o sistema gera um erro e não permite que o novo registro seja criado.

Além dos dois métodos já citados, foi requisitado que a API pudesse receber requisições GET, PUT e DELETE dentro das URIs específicas para cada transação, sendo definidas por `/receitas/{id}` e `/despesas/{id}`. Foram efetuados testes nas URIs específicas, porém será exibido apenas para a URI `/receitas/{id}`.

Primeiramente foi efetuada uma requisição GET para a URI da transação.

![image](https://user-images.githubusercontent.com/6025360/183138294-d25cba88-4862-4752-8ebf-2e851f554ea3.png)

Após isso, foi alterado o valor registrado da transação com o método PUT. Assim como na URI `/receitas`, o método PUT não irá aceitar valores duplicados de `descricao` dentro de um mesmo mês.

![image](https://user-images.githubusercontent.com/6025360/183138532-26fd5423-48a8-4483-9754-d0cdeb337cd5.png)

Por último, foi deletada a entrada no sistema. Essa exclusão de deu pelo método DELETE e para confirmar, foi novamnete efetuada uma requisição GET para a URI de receitas.

![image](https://user-images.githubusercontent.com/6025360/183138699-dc592ee2-9d6b-4ada-bd4c-5736e64605b5.png)

![image](https://user-images.githubusercontent.com/6025360/183138723-7a457dde-88d1-424d-a14d-e368c768d279.png)

Com a API testada, é possível seguir para os próximos passos da aplicação.

### Novas funcionalidades

Na segunda semana, a empresa entrou em contato e pediu algumas melhorias na API. As melhorias requisitadas foram incluir uma categorização para as receitas, busca de receitas e despesas de acordo com a descrição, listagem de receitas e despesas de um determinado mes e um resumo mensal detalhado.

Para a categorização das despesas, a empresa pediu que houvessem 8 categorias presentes. Para implementar, foi incluída uma nova variável no banco de dados, que receberá a informação da categoria da despesa. Essa nova variável tera também um valor padrão.

```python
  ...
  class Despesa(models.Model):
      categorias = (
          ('A', 'Alimentação'),
          ('S', 'Saúde'),
          ('M', 'Moradia'),
          ('T', 'Transporte'),
          ('E', 'Educação'),
          ('L', 'Lazer'),
          ('I', 'Imprevistos'),
          ('O', 'Outras')
      )

      categoria = models.CharField(max_length = 3, choices=categorias, default='O')
  ...
```

Para a criação de um mecanismo de busca, a empresa requisitou que essa funcionalidade se desse pelo meio de uma URI `/despesas?descricao=texto`. Essa busca foi implementada com o módulo django-filters. Também podem ser incluidos outros filtros, caso desejável pela empresa.

```python
  class ReceitasViewSet(viewsets.ModelViewSet):
      """Listando todas as receitas"""
      
      queryset = Receita.objects.all()
      serializer_class = ReceitaSerializer
      filter_backends = [DjangoFilterBackend, filters.SearchFilter]
      search_fields = ['descricao']
```
 A biblioteca, no entanto, cria uma url com o final `?search=`. Isso teve que ser alterado nas configurações do programa.

 ```python
  REST_FRAMEWORK = {
      'SEARCH_PARAM': 'descricao',
}
 ```

Para o resumo do mês, foi criado um novo viewset, que irá receber os registros das receitas e das despesas de acordo com o mês e ano.

```python
class ResumoAnoMesViewSet(viewsets.ViewSet):
    """Listando um resumo de receitas e despesas por ano e mês."""

    queryset = Receita.objects.none()

    def list(self, request, ano, mes):
        soma_receitas = Receita.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor')) ['valor__sum'] or 0
        soma_despesas = Despesa.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor')) ['valor__sum'] or 0
        despesa_por_categoria = Despesa.objects.filter(data__year=ano, data__month=mes).values('categoria').annotate(Total = Sum('valor'))
        saldo = soma_receitas - soma_despesas

        return Response({
            'Valor recebido': soma_receitas,
            'Valor gasto': soma_despesas,
            'Saldo do mês': saldo,
            'Despesa por categoria': despesa_por_categoria
        })
```

Por último, após os testes manuais feitos por meio do postman, a empresa requisitou que fossem desenvolvidos testes automatizados. Serão feitos testes de unidade e de integração. Além de outros testes que possam ser necessários. Esses testes serão criados após o desenvolvimento das funcionalidades requisitadas na próxima semana.

### Usuários

Na terceira e última semana, a empresa requisitou que apenas usuários autenticados possam acessar a API. A título de testes foram criados usuários por meio da administração do django, sem criar um CRUD novo para os usuários. Além do pedido da empresa, também foi definida uma regra de negócio para que as receitas, despesas e resumos apresentadas nos endpoints sejam apenas do usuário que está logado no momento. Caso o usuário não esteja logado, será requisitado um login.

Para implementar a funcionalidade, foi utilizado um tutorial do [django rest](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/). Em conjunto com isso, foram criados dois usuários, que contém registros no banco de dados por meio de uma chave primária.

```python
class Receita(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='receitas', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200, unique_for_month='data', blank=False)
    valor = models.DecimalField(max_digits = 10, decimal_places=2, blank=False)
    data = models.DateField(blank=False)

    def __str__(self):
        return self.descricao
```

Também foi criado um serializer para os usuários. Esse serializer permite encontrar as receitas e despesas por usuário.

```python
class UsuarioSerializer(serializers.ModelSerializer):

    receitas = serializers.PrimaryKeyRelatedField(many=True, queryset=Receita.objects.all())
    despesas = serializers.PrimaryKeyRelatedField(many=True, queryset=Despesa.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'receitas', 'despesas']
```

Após essa mudança, os viewsets foram alterados para exibir apenas as informações de acordo com o usuário logado no momento.

```python
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
```

Por último, foram incluidos novos endpoints para tentar um crud de usuarios e efetuar o login na aplicação.

```python
urls
```

### Testes automatizados

Além dos testes feitos com o postman na primeira semana, a empresa requisitou também que fossem feitos testes automatizados para verificar se as regras de negócio estão funcionando conforme o esperado. Além dos testes automatizados dos endpoints, foram criados também outros testes de integração e de unidade.

Os testes foram feitos utilizando o método TestCase do django. Os testes foram feitos e armazenados em na pasta `'tests'` e separados de acordo com o arquivo que estava sendo testado.

Primeiramente foram testados os modelos desenvolvidos, com o intuito de verificar a integridade das informações passadas aos banco de dados. Foram feitos testes para os dois modelos, criando uma transação específica para os testes e conferindo se as informções passadas estavam corretas no banco de dados.

```python
...
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
...
```

### Deploy

Além disso, foi requisitado o deploy da API em algum servidor cloud. Para esse projeto foi utilizado o Heroku.



## Entre em contato

LinkedIn: https://www.linkedin.com/in/viniciuspf/

E-mail: vinicius-pf@outlook.com