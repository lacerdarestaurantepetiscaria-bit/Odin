from decimal import Decimal
from django.db import models
from apps.customers.models import Customer
from apps.products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [("aberto","Aberto"),("preparo","Em preparo"),("pronto","Pronto"),("entregue","Entregue"),("cancelado","Cancelado")]
    SERVICE_CHOICES = [("mesa","Mesa"),("balcao","Balcão"),("delivery","Delivery"),("retirada","Retirada")]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    table_number = models.CharField("Mesa", max_length=20, blank=True)
    service_type = models.CharField("Tipo de atendimento", max_length=20, choices=SERVICE_CHOICES, default="mesa")
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="aberto")
    notes = models.TextField("Observações", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-created_at"]
    def __str__(self):
        return f"Pedido {self.pk}"
    @property
    def total(self):
        return sum((item.total for item in self.items.all()), Decimal("0.00"))

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE, verbose_name="Pedido")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produto")
    quantity = models.PositiveIntegerField("Quantidade", default=1)
    unit_price = models.DecimalField("Preço unitário", max_digits=10, decimal_places=2)
    @property
    def total(self):
        return self.unit_price * self.quantity
