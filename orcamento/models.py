from django.core.exceptions import ValidationError
from django.db import models


class Receita(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='receitas', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200, blank=False)
    valor = models.DecimalField(max_digits = 10, decimal_places=2, blank=False)
    data = models.DateField(blank=False)

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        if Receita.objects.filter(descricao = self.descricao, data__year = self.data.year, data__month=self.data.month, usuario=self.usuario):
            raise ValidationError("Descrição já cadastrada no mês")
        
        super(Receita, self).save()

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

    usuario = models.ForeignKey('auth.User', related_name='despesas', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200, unique_for_month='data', blank=False)
    valor = models.DecimalField(max_digits = 10, decimal_places=2, blank=False)
    data = models.DateField(blank=False)
    categoria = models.CharField(max_length = 3, choices=categorias, default='O')

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        if Despesa.objects.filter(descricao = self.descricao, data__year = self.data.year, data__month=self.data.month, usuario=self.usuario):
            raise ValidationError("Descrição já cadastrada no mês")
        
        super(Receita, self).save()

