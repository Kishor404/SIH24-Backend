# Generated by Django 5.1.3 on 2024-11-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=200)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('seller', 'Seller'), ('driver', 'Driver'), ('customer', 'Customer')], default='customer', max_length=20)),
            ],
        ),
    ]
