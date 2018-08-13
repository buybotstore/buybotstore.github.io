# Generated by Django 2.0.7 on 2018-08-11 18:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BuyBots_app', '0008_auto_20180810_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='image_path',
        ),
        migrations.AddField(
            model_name='bot',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deal',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]