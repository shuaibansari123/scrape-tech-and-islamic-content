# Generated by Django 5.1.1 on 2024-12-14 11:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "ImfeelingApp",
            "0022_battle_created_at_battle_image_battle_image_url_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="imfeeling",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imfeeling",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]