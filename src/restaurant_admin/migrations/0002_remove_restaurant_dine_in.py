# Generated by Django 3.0.6 on 2020-06-29 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='dine_in',
        ),
    ]
