# Generated by Django 5.1.1 on 2024-12-05 18:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ImfeelingApp", "0015_muhammadchildren"),
    ]

    operations = [
        migrations.CreateModel(
            name="Battle",
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