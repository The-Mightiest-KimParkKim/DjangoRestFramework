# Generated by Django 3.1.4 on 2020-12-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0003_auto_20201217_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
