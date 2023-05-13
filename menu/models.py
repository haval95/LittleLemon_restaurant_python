from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name


class Menu_Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_ingridiants = models.CharField(max_length=500)
    item_price = models.IntegerField()
    category_id = models.name = models.ForeignKey(
        Category, related_name="category_name", on_delete=models.PROTECT, default=None
    )

    def __str__(self) -> str:
        return self.item_name
