# Generated by Django 4.2.1 on 2023-05-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="table",
            fields=[
                (
                    "table_number",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("table_location", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
