# Generated by Django 5.1.3 on 2024-11-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='device_id',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
