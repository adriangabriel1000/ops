# Generated by Django 4.2.15 on 2024-09-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manplan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.AddField(
            model_name='schedule',
            name='position',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
