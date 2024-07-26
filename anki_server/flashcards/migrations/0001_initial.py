# Generated by Django 5.0.7 on 2024-07-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flashcard",
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
                ("question", models.CharField(max_length=255)),
                ("answer", models.TextField()),
            ],
        ),
    ]
