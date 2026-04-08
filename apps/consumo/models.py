from django.db import models
from apps.orders.models import Order
from apps.products.models import Product
from apps.estoque.models import Supply

class StockConsumption(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="stock_consumptions", verbose_name="Pedido")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name="Insumo")
    quantity_consumed = models.DecimalField("Quantidade consumida", max_digits=12, decimal_places=3, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Consumo de estoque"
        verbose_name_plural = "Consumos de estoque"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Pedido {self.order_id} - {self.supply} ({self.quantity_consumed})"
