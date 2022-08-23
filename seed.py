import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from orcamento.models import  Receita, Despesa

def criando_receitas(quantidade_de_receitas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_receitas):
        descricao = fake.name()
        valor = round(random.randint(1, 1000) * random.random(), 2)
        data = fake.date_between(start_date='-6m', end_date='today')
        a = Receita(descricao=descricao,valor=valor, data=data)
        a.save()

def criando_despesas(quantidade_de_despesas):
    fake = Faker('pt_BR')
    Faker.seed(100)
    for _ in range(quantidade_de_despesas):
        descricao = fake.name()
        valor = round(random.randint(1, 1000) * random.random(), 2)
        data = fake.date_between(start_date='-6m', end_date='today')
        categoria = random.choice("ASMTELIO")

        a = Despesa(descricao=descricao,valor=valor, data=data, categoria=categoria)
        
        a.save()


criando_despesas(50)
criando_receitas(50)