from django.db import models
from menu.models import Menu_Item


class table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    table_location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.table_number}"
    


class order (models.Model):
    table_number = models.ForeignKey(table, related_name='table', on_delete=models.PROTECT)
    ord_date_created = models.DateTimeField(auto_now_add=True)
    ord_date_deliverd = models.DateTimeField(auto_now_add=True)
    is_deliverd = models.BooleanField(default=False)
    is_taken = models.BooleanField(default=False)
    ord_items = models.ManyToManyField(Menu_Item)
    
   