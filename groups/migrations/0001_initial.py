# Generated by Django 5.0.6 on 2024-05-21 21:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField(allow_unicode=True, unique=True)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "description_html",
                    models.TextField(blank=True, default="", editable=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GroupMember",
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
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="groups.group",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_groups",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("group", "user")},},
        ),
        migrations.AddField(
            model_name="group",
            name="memebers",
            field=models.ManyToManyField(
                through="groups.GroupMember", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
