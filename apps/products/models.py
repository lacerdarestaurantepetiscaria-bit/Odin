from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES = [
        ("acompanhamento", "Acompanhamento"),
        ("carne", "Carne"),
        ("bebida", "Bebida"),
        ("sobremesa", "Sobremesa"),
        ("outro", "Outro"),
    ]
    name = models.CharField("Nome", max_length=120, unique=True)
    category = models.CharField("Categoria", max_length=30, choices=CATEGORY_CHOICES, default="outro")
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["name"]
    def __str__(self):
        return self.name
