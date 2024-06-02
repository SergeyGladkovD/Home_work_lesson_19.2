# Generated by Django 5.0.4 on 2024-06-01 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_rename_image_product_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                (
                    "num_version",
                    models.PositiveIntegerField(verbose_name="номер версии"),
                ),
                ("name_version", models.TextField(verbose_name="название версии")),
                (
                    "indicates_current_version",
                    models.BooleanField(
                        default=True, verbose_name="признак текущей версии."
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank="True",
                        null="True",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия",
                "verbose_name_plural": "версии",
            },
        ),
    ]