# Generated by Django 5.1.1 on 2024-10-08 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                (
                    "subject",
                    models.CharField(max_length=250, verbose_name="тема письма"),
                ),
                ("body", models.TextField(verbose_name="тело письма")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="MailingSettings",
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
                (
                    "start_from",
                    models.DateTimeField(verbose_name="Дата и время начала рассылки"),
                ),
                (
                    "next_sending",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата следующей рассылки"
                    ),
                ),
                (
                    "end_on",
                    models.DateTimeField(
                        verbose_name="Дата и время окончания рассылки"
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("daily", "Раз в день"),
                            ("weekly", "Раз в неделю"),
                            ("monthly", "Раз в месяц"),
                        ],
                        max_length=10,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("completed", "Завершена"), ("created", "Создана")],
                        default="created",
                        max_length=20,
                        verbose_name="Статус рассылки",
                    ),
                ),
                (
                    "clients",
                    models.ManyToManyField(
                        related_name="clients",
                        to="client.client",
                        verbose_name="клиенты",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.message",
                        verbose_name="сообщение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Настройка рассылки",
                "verbose_name_plural": "Настройки рассылок",
            },
        ),
        migrations.CreateModel(
            name="Log",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время попытки"
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=False, verbose_name="статус попытки"),
                ),
                (
                    "response",
                    models.TextField(
                        default="Ответ не получен",
                        verbose_name="ответ почтового сервера",
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mailing_settings",
                        to="mailing.mailingsettings",
                        verbose_name="id_рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лог",
                "verbose_name_plural": "Логи",
            },
        ),
    ]
