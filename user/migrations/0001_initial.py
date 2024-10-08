# Generated by Django 5.1 on 2024-08-13 16:45

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
            name="Profile",
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
                ("initals", models.CharField(max_length=10)),
                ("unique", models.CharField(blank=True, max_length=200)),
                ("address", models.CharField(blank=True, max_length=200)),
                ("idnum", models.CharField(blank=True, max_length=200)),
                ("cell", models.CharField(blank=True, max_length=200)),
                ("homenum", models.CharField(blank=True, max_length=200)),
                ("dob", models.DateTimeField(blank=True)),
                ("designation", models.CharField(blank=True, max_length=200)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="profilepic.jpg",
                        upload_to="profile_pictures",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
