from django.contrib import admin
from orcamento.models import Receita, Despesa

# Register your models here.

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 10

admin.site.register(Receita, Receitas)

class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 20

admin.site.register(Despesa, Despesas)
