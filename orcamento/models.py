from django.db import models

# Create your models here.

class Receita(models.Model):
    descricao = models.CharField(max_length=200, unique_for_month='data', blank=False)
    valor = models.DecimalField(max_digits = 10, decimal_places=2, blank=False)
    data = models.DateField(blank=False)

    def __str__(self):
        return self.descricao

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

    descricao = models.CharField(max_length=200, unique_for_month='data', blank=False)
    valor = models.DecimalField(max_digits = 10, decimal_places=2, blank=False)
    data = models.DateField(blank=False)
    categoria = models.CharField(max_length = 3, choices=categorias, default='O')

    def __str__(self):
        return self.descricao

