# Generated by Django 5.1.1 on 2024-12-06 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ImfeelingApp", "0019_surahcontent"),
    ]

    operations = [
        migrations.CreateModel(
            name="Surah",
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
                ("title", models.CharField(max_length=100)),
                ("number", models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SurahTranslation",
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
                ("language", models.CharField(max_length=50)),
                ("content", models.TextField()),
                ("recitator_by", models.CharField(max_length=100)),
                (
                    "surah",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ImfeelingApp.surah",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="SurahContent",
        ),
    ]
