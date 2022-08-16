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

Na segunda semana, a empresa entrou em contato e pediu algumas melhorias na API.

### Autenticação importante

Na última semana, a empresa requisitou que apenas usuários autenticados possam acessar a API.

## Entre em contato

LinkedIn: https://www.linkedin.com/in/viniciuspf/

E-mail: vinicius-pf@outlook.com