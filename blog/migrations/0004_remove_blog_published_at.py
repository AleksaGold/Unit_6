# Generated by Django 4.2.2 on 2024-10-11 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blog_published_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="published_at",
        ),
    ]
