# Generated by Django 5.1.1 on 2024-11-29 16:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ImfeelingApp", "0002_imfeeling_description_imfeeling_feeling_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="DuaDhikr",
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
                ("title", models.CharField(max_length=255)),
                ("description", ckeditor.fields.RichTextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]