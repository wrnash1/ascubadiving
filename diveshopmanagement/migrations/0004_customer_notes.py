# Generated by Django 4.2.1 on 2023-05-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diveshopmanagement", "0003_remove_customer_notes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="notes",
            field=models.TextField(default="None"),
        ),
    ]
