from django.contrib import admin
from django.urls import path, include
from orcamento.views import ReceitasViewSet, DespesasViewSet, ListaReceitasMesViewSet, ListaDespesasMesViewSet, ResumoAnoMesViewSet
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')

schema_view = get_schema_view(
   openapi.Info(
      title="API de controle financeiro",
      default_version='v1',
      description="API de controle financeiro residencial, com informações de receitas, despesas e saldos mensais.",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:year>/<int:month>', ListaReceitasMesViewSet.as_view({'get':'list'})),
    path('despesas/<int:year>/<int:month>', ListaDespesasMesViewSet.as_view({'get':'list'})),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('resumo/<int:ano>/<int:mes>', ResumoAnoMesViewSet.as_view({'get':'list'})),
]