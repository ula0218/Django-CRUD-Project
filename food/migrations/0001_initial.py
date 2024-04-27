# Generated by Django 5.0.4 on 2024-04-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("food", models.CharField(max_length=100)),
                ("price", models.CharField(max_length=1000000)),
                ("date", models.CharField(max_length=100)),
            ],
        ),
    ]
