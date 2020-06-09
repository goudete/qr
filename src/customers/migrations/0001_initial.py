# Generated by Django 3.0.6 on 2020-06-09 17:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('cash_code', models.CharField(max_length=255, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('stripe_order_id', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tip', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('custom_tip', models.BooleanField(default=False)),
                ('total_with_tip', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('email', models.EmailField(max_length=200)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurant_admin.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('custom_instructions', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=255, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Cart')),
            ],
        ),
    ]
