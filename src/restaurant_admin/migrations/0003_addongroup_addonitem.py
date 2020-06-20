# Generated by Django 3.0.6 on 2020-06-19 23:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0002_auto_20200619_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOnGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Name')),
                ('menu_items', models.ManyToManyField(to='restaurant_admin.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='AddOnItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Price')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.AddOnGroup')),
            ],
        ),
    ]
