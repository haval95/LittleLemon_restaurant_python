from django.db import models
from menu.models import Menu_Item


class table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    table_location = models.CharField(max_length=100, blank=True)
    


class order (models.Model):
    table_number = models.ForeignKey(table, related_name='table', on_delete=models.PROTECT)
    ord_date_created = models.DateTimeField(auto_now_add=True)
    ord_date_deliverd = models.DateTimeField(auto_now_add=True)
    ord_items = models.ManyToManyField(Menu_Item)