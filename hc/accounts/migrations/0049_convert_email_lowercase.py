# Generated by Django 5.1.1 on 2024-10-24 08:53

from __future__ import annotations

from typing import Any

from django.apps.registry import Apps
from django.core.management import CommandError
from django.db import migrations
from django.db.models.functions import Lower


def convert_emails(apps: Apps, schema_editor: Any) -> None:
    User = apps.get_model("auth", "User")
    # A queryset of users with non-lowercase email addresses
    problematic_users = User.objects.exclude(email=Lower("email"))

    # For each affected user, check if their normalized email address would
    # conflict with another user's normalized email address.
    # The situation we want to protect against is where before migration we have:
    # * Alice@Example.Org
    # * ALICE@EXAMPLE.ORG
    # And after migration we have
    # * alice@example.org
    # * alice@example.org
    # (Two accounts with the same email address).
    for u in problematic_users:
        q = User.objects.exclude(id=u.id).filter(email__iexact=u.email)
        if conflicting_user := q.first():
            raise CommandError(
                f"Cannot convert {u.email} to lower case because of an existing "
                f"account with a conflicting email address: {conflicting_user.email}"
            )

    # If no conflicts, go ahead and do a mass update
    problematic_users.update(email=Lower("email"))


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0048_alter_profile_user"),
    ]

    operations = [
        migrations.RunPython(convert_emails, migrations.RunPython.noop),
    ]
