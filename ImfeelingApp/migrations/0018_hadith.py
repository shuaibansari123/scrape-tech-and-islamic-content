# Generated by Django 5.1.1 on 2024-12-06 05:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ImfeelingApp", "0017_wife"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hadith",
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
                ("content", ckeditor.fields.RichTextField()),
            ],
        ),
    ]