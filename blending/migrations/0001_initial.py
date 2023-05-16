# Generated by Django 4.2 on 2023-05-16 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Gas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("oxygen_percentage", models.FloatField()),
                ("helium_percentage", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="BlendComponent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("percentage", models.FloatField()),
                (
                    "blend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blending.blend"
                    ),
                ),
                (
                    "gas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blending.gas"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="blend",
            name="gases",
            field=models.ManyToManyField(
                through="blending.BlendComponent", to="blending.gas"
            ),
        ),
    ]
