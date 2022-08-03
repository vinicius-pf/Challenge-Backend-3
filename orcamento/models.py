from django.db import models

# Create your models here.

class Receita(models.Model):
    descricao = models.CharField(max_length=200, unique_for_month='data')
    valor = models.DecimalField(max_digits = 10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    descricao = models.CharField(max_length=200, unique_for_month='data')
    valor = models.DecimalField(max_digits = 10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao