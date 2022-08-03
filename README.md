# Alura Challenge Back-End 4ª Edição

Neste Repositório estão os meus projetos desenvolvidos no mês de Agosto 2022 como parte da quarta edição do [Alura Challenge Back-End](https://www.alura.com.br/challenges/back-end-4/). 

* [Sobre o Challenge](#sobre-o-challenge)
* [Projetos desenvolvidos](#projetos-desenvolvidos)
* [Entre em Contato](#entre-em-contato)

## Sobre o Challenge

## Projetos desenvolvidos

Inicialmente foi criada uma venv para a criação e testes da API. Nela foram instaladas as ferramentas Django e Django REST Framework. Para efetuar testes foi utilizado o PostMan.
Nas configurações iniciais, foi criado um projeto 'setup' e foram alteradas algumas configurações: 

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

para a criação da API, foi criada uma aplicação 'orcamento' que irá ser a base.

Para o banco de dados, foi utilizado um banco de dados PostgreSQL, utilizando do modulo psycopg2. para manter as informações sensíveis secretas, foi utilizado o módulo python-decouple

Para o início da criação da API, foi requisitado que a API tivesse duas tabelas, uma de receita e outra de despesas, que ao ser consultada retornaria as informações por meio de um arquivo tipo JSON. Para isso, foram utilizadas os métodos do Django REST framework.

Criação dos modelos

Validação no admin

migrando

após isso, foi verificada, por meio do admin do django, se as informações estavam sendo salvas no banco de dados.

mostrando que funciona

Para que as informações pudessem ser visualizadas como formato json, foi criado um serializer que irá listar as informações das tabelas

Serializer

Para visualizar em uma url personalizada, primeiro foram criados modelos viewsets 

Views

Após a criação das viewsets, é necessario validar as urls com um router para exibição das informações com urls personalizadas.

Url

Durante o processo, foram efetuados testes diretamente pela página que o framework gera. Além disso, também foi utilizado o postman para verificar as principais funcionalidades da API.




## Entre em contato

LinkedIn: https://www.linkedin.com/in/viniciuspf/

E-mail: vinicius-pf@outlook.com






