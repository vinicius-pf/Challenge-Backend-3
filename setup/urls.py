from django.contrib import admin
from django.urls import path, include
from orcamento.views import ReceitasViewSet, DespesasViewSet, ListaReceitasMesViewSet, ListaDespesasMesViewSet, ResumoAnoMesViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')
router.register('resumo', ResumoAnoMesViewset, basename='Resumo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:year>/<int:month>', ListaReceitasMesViewSet.as_view({'get':'list'})),
    path('despesas/<int:year>/<int:month>', ListaDespesasMesViewSet.as_view({'get':'list'}))
]
