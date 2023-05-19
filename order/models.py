from django.db import models


class table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    table_location = models.CharField(max_length=100, blank=True)
    


