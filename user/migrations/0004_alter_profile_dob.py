# Generated by Django 5.1 on 2024-08-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_profile_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="dob",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
