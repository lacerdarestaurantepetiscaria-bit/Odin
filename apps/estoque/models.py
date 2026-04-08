from django.db import models

class Supply(models.Model):
    CATEGORY_CHOICES = [
        ("alimenticio", "Alimentício"),
        ("bebida", "Bebida"),
        ("descartavel", "Descartável"),
        ("limpeza", "Limpeza"),
        ("outro", "Outro"),
    ]
    UNIT_CHOICES = [
        ("kg", "Kg"),
        ("g", "Grama"),
        ("l", "Litro"),
        ("ml", "Mililitro"),
        ("un", "Unidade"),
    ]

    name = models.CharField("Nome", max_length=120, unique=True)
    category = models.CharField("Categoria", max_length=30, choices=CATEGORY_CHOICES, default="outro")
    unit = models.CharField("Unidade", max_length=10, choices=UNIT_CHOICES, default="un")
    quantity = models.DecimalField("Quantidade em estoque", max_digits=12, decimal_places=3, default=0)
    cost = models.DecimalField("Custo unitário", max_digits=10, decimal_places=2, default=0)
    minimum_quantity = models.DecimalField("Estoque mínimo", max_digits=12, decimal_places=3, default=0)
    is_active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def is_low(self):
        return self.quantity <= self.minimum_quantity
