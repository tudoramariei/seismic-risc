# Generated by Django 2.2.4 on 2019-09-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('map_app', '0005_auto_20190916_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='sector',
            field=models.CharField(choices=[('Sector 1', 'Sector 1'),
                                            ('Sector 2', 'Sector 2'),
                                            ('Sector 3', 'Sector 3'),
                                            ('Sector 4', 'Sector 4'),
                                            ('Sector 5', 'Sector 5'),
                                            ('Sector 6', 'Sector 6')], max_length=20),
        ),
    ]
