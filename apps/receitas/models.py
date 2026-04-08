from decimal import Decimal
from django.db import models
from apps.products.models import Product
from apps.estoque.models import Supply

class RecipeItem(models.Model):
    product = models.ForeignKey(Product, related_name="recipe_items", on_delete=models.CASCADE, verbose_name="Produto")
    supply = models.ForeignKey(Supply, related_name="recipe_items", on_delete=models.CASCADE, verbose_name="Insumo")
    quantity_used = models.DecimalField("Quantidade usada", max_digits=12, decimal_places=3, default=0)

    class Meta:
        verbose_name = "Item da ficha técnica"
        verbose_name_plural = "Itens da ficha técnica"
        unique_together = ("product", "supply")
        ordering = ["product__name", "supply__name"]

    def __str__(self):
        return f"{self.product} -> {self.supply} ({self.quantity_used})"

    @property
    def estimated_cost(self):
        return (self.quantity_used or Decimal("0")) * (self.supply.cost or Decimal("0"))
