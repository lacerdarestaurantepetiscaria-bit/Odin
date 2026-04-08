from decimal import Decimal
from django.db import models

class CashSession(models.Model):
    STATUS_CHOICES = [
        ("aberto", "Aberto"),
        ("fechado", "Fechado"),
    ]
    opening_amount = models.DecimalField("Abertura", max_digits=10, decimal_places=2, default=0)
    closing_amount = models.DecimalField("Fechamento", max_digits=10, decimal_places=2, default=0)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="aberto")
    notes = models.TextField("Observações", blank=True)
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Sessão de caixa"
        verbose_name_plural = "Sessões de caixa"
        ordering = ["-opened_at"]

    def __str__(self):
        return f"Caixa {self.id} - {self.status}"

    @property
    def expected_total(self):
        from apps.payments.models import Payment
        payments_total = sum((p.amount for p in Payment.objects.all()), Decimal("0.00"))
        return self.opening_amount + payments_total
