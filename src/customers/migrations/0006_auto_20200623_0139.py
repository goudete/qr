# Generated by Django 3.0.6 on 2020-06-23 01:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20200622_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemcounter',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
