# Generated by Django 3.0.6 on 2020-08-09 21:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOnGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Name')),
                ('photo_path', models.CharField(max_length=255, null=True)),
                ('qr_code_path', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Restaurant Name')),
                ('info', models.TextField(max_length=255, null=True, verbose_name='Additional Info')),
                ('photo_path', models.CharField(max_length=255, null=True)),
                ('about', models.TextField(max_length=255, null=True, verbose_name="Your Restaurant's Vision")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kitchen_login_no', models.IntegerField(null=True, unique=True)),
                ('answered_pay_question', models.BooleanField(default=False)),
                ('handle_payment', models.BooleanField(null=True)),
                ('info_input', models.BooleanField(default=False)),
                ('stripe_account_id', models.CharField(default='', max_length=255, null=True)),
                ('dine_in', models.BooleanField(default=False)),
                ('language', models.CharField(default='en-us', max_length=10)),
                ('opening_time', models.TimeField(null=True)),
                ('closing_time', models.TimeField(null=True)),
                ('order_stream_email', models.EmailField(max_length=254, null=True)),
                ('order_stream', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SelectOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('menus', models.ManyToManyField(to='restaurant_admin.Menu')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Name')),
                ('description', models.TextField(default='', null=True, verbose_name='Description')),
                ('category', models.CharField(default='', max_length=200, verbose_name='Category')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Price')),
                ('photo_path', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_in_stock', models.BooleanField(default=True)),
                ('menus', models.ManyToManyField(to='restaurant_admin.Menu')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.Restaurant'),
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
        migrations.AddField(
            model_name='addongroup',
            name='menu_items',
            field=models.ManyToManyField(to='restaurant_admin.MenuItem'),
        ),
        migrations.AddField(
            model_name='addongroup',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant_admin.Restaurant'),
        ),
    ]
