from django.db import models
from apps.orders.models import Order
class Payment(models.Model):
    METHOD_CHOICES = [("dinheiro","Dinheiro"),("cartao","Cartão"),("pix","Pix"),("voucher","Voucher"),("fiado","Fiado")]
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name="payments", verbose_name="Pedido")
    method = models.CharField("Método", max_length=20, choices=METHOD_CHOICES)
    amount = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    notes = models.CharField("Observação", max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
        ordering = ["-created_at"]
