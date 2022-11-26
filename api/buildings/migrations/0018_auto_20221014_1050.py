# Generated by Django 3.2.15 on 2022-10-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0017_auto_20220112_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='consolidated_buildings',
            field=models.IntegerField(null=True, verbose_name='consolidated buildings'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='evaluated_buildings',
            field=models.IntegerField(null=True, verbose_name='evaluated buildings'),
        ),
    ]