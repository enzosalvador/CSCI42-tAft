# Generated by Django 5.0.3 on 2024-03-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserModel",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=50)),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                ("email", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("height", models.IntegerField()),
                ("weight", models.IntegerField()),
            ],
        ),
    ]
