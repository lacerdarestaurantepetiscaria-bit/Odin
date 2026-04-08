from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("produtos/", include("apps.products.urls")),
    path("clientes/", include("apps.customers.urls")),
    path("pedidos/", include("apps.orders.urls")),
    path("pagamentos/", include("apps.payments.urls")),
    path("odin-ia/", include("apps.ai_assistant.urls")),
    path("pdv/", include("apps.pdv.urls")),
    path("salao/", include("apps.salon.urls")),
    path("cozinha/", include("apps.kds.urls")),
    path("caixa/", include("apps.caixa.urls")),
    path("entrega/", include("apps.entrega.urls")),
    path("estoque/", include("apps.estoque.urls")),
    path("receitas/", include("apps.receitas.urls")),
    path("whatsapp/", include("apps.whatsapp.urls")),
    path("painel-dono/", include("apps.analytics.urls")),
    path("alertas/", include("apps.alerts.urls")),
    path("automacoes/", include("apps.automacoes.urls")),
]
