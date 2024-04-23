# Generated by Django 5.0.3 on 2024-04-23 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("userprofile", "0003_alter_userprofilemodel_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ForumPost",
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
                ("title", models.CharField(max_length=50)),
                ("body", models.TextField(max_length=1000)),
                (
                    "pub_datetime",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Published Date and Time"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userprofile.userprofilemodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reply",
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
                ("body", models.CharField(max_length=1000)),
                (
                    "pub_datetime",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Published Date and Time"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userprofile.userprofilemodel",
                    ),
                ),
                (
                    "forum_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="forum.forumpost",
                    ),
                ),
            ],
        ),
    ]