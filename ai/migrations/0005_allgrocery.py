# Generated by Django 3.1.2 on 2020-12-09 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0004_auto_20201209_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllGrocery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'ALL_GROCERY',
            },
        ),
    ]
