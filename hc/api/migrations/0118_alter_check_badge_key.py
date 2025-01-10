# Generated by Django 5.1.4 on 2024-12-27 10:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0117_fill_badge_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='badge_key',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
