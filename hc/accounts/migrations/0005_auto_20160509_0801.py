# Generated by Django 1.9 on 2016-05-09 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0004_profile_api_key"),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="team_access_allowed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="team_name",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="member",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.Profile"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
