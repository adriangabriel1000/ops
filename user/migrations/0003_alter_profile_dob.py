# Generated by Django 5.1 on 2024-08-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_profile_initals"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="dob",
            field=models.DateTimeField(null=True),
        ),
    ]
