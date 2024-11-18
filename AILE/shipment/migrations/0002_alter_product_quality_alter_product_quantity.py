# Generated by Django 5.1.3 on 2024-11-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quality',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]