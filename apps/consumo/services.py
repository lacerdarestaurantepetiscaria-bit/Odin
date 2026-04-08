from decimal import Decimal
from apps.consumo.models import StockConsumption
from apps.receitas.models import RecipeItem

def apply_stock_consumption(order):
    if getattr(order, "_stock_applied", False):
        return
    existing = order.stock_consumptions.exists()
    if existing:
        return
    for order_item in order.items.select_related("product").all():
        recipe_items = RecipeItem.objects.select_related("supply").filter(product=order_item.product)
        for recipe in recipe_items:
            qty = (recipe.quantity_used or Decimal("0")) * order_item.quantity
            supply = recipe.supply
            supply.quantity = (supply.quantity or Decimal("0")) - qty
            supply.save(update_fields=["quantity"])
            StockConsumption.objects.create(
                order=order,
                product=order_item.product,
                supply=supply,
                quantity_consumed=qty,
            )
