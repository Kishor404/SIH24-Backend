# Generated by Django 5.1.3 on 2024-11-20 02:00

import routes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.CharField(max_length=200)),
                ('seller_id', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=200)),
                ('source', models.JSONField(validators=[routes.models.validate_coordinates])),
                ('destination', models.JSONField(validators=[routes.models.validate_coordinates])),
                ('current_location', models.JSONField(validators=[routes.models.validate_coordinates])),
                ('halt', models.JSONField(validators=[routes.models.validate_halt_data])),
            ],
        ),
    ]
