# Generated by Django 4.2 on 2023-05-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diveshopmanagement", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="level",
            name="certification_level",
            field=models.CharField(
                choices=[
                    ("OW", "Open Water"),
                    ("AOW", "Advanced Open Water"),
                    ("RD", "Rescue Diver"),
                    ("DM", "Dive Master"),
                    ("AI", "Assistant Instructor"),
                    ("OWSI", "Open Water Scuba Instructor"),
                    ("MSDT", "Master Scuba Diver Trainer"),
                    ("IDC", "Instructor Development Course"),
                    ("IE", "Instructor Examination"),
                    ("MI", "Master Instructor"),
                    ("CD", "Course Director"),
                    ("IT", "Instructor Trainer"),
                    ("CIT", "Course Director Trainer"),
                ],
                max_length=50,
            ),
        ),
    ]
