# Generated by Django 5.1.3 on 2024-11-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(default='0', max_length=200)),
                ('reading_temperature', models.CharField(max_length=200)),
                ('reading_humidity', models.CharField(max_length=200)),
                ('maintain_temperature', models.CharField(max_length=200)),
                ('maintain_humidity', models.CharField(max_length=200)),
            ],
        ),
    ]