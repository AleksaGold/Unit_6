# Generated by Django 4.2.2 on 2024-10-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0002_mailingsettings_owner_message_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailingsettings",
            options={
                "permissions": [("can_change_status", "Can change status")],
                "verbose_name": "Настройка рассылки",
                "verbose_name_plural": "Настройки рассылок",
            },
        ),
    ]
