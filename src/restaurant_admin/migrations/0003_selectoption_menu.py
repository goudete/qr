# Generated by Django 3.0.6 on 2020-06-16 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0002_auto_20200616_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectoption',
            name='menu',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.Menu'),
            preserve_default=False,
        ),
    ]
