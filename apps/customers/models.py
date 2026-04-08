from django.db import models
class Customer(models.Model):
    name = models.CharField("Nome", max_length=120)
    phone = models.CharField("Telefone", max_length=30, blank=True)
    address = models.CharField("Endereço", max_length=255, blank=True)
    neighborhood = models.CharField("Bairro", max_length=120, blank=True)
    reference = models.CharField("Referência", max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["name"]
    def __str__(self):
        return self.name
