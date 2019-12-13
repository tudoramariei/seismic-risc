# Generated by Django 2.2.4 on 2019-11-23 11:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_building_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
