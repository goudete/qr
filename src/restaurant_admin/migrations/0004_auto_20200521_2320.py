# Generated by Django 3.0.6 on 2020-05-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0003_auto_20200520_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='info',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='photo_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
