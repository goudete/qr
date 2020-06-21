# Generated by Django 3.0.6 on 2020-06-20 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0003_addongroup_addonitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addonitem',
            name='group',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menus',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.Menu'),
        ),
        migrations.DeleteModel(
            name='AddOnGroup',
        ),
        migrations.DeleteModel(
            name='AddOnItem',
        ),
    ]
