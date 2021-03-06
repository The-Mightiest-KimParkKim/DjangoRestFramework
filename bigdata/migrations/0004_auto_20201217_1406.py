# Generated by Django 3.1.4 on 2020-12-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0003_auto_20201217_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommrecipe',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='howto',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='img',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='ingredient',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='ingredient_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='purpose',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='seasoning',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='recommrecipe',
            name='seasoning_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
