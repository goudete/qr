# Generated by Django 3.0.6 on 2020-06-22 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0005_auto_20200621_1923'),
        ('customers', '0002_menuitemcounter_addon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemcounter',
            name='addon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.AddOnItem'),
        ),
    ]
