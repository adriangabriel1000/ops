# Generated by Django 4.2.15 on 2024-08-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0002_shift_alter_cycle_shift'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycle',
            name='shift',
        ),
        migrations.AddField(
            model_name='cycle',
            name='shift',
            field=models.ManyToManyField(to='cycle.shift'),
        ),
    ]
