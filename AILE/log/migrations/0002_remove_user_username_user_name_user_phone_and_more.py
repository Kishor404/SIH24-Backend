# Generated by Django 5.1.3 on 2024-11-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=None, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
