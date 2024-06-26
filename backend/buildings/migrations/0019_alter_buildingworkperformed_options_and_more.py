# Generated by Django 4.2.1 on 2023-05-30 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("buildings", "0018_auto_20221014_1050"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="buildingworkperformed",
            options={
                "verbose_name": "type of work performed",
                "verbose_name_plural": "types of work performed",
            },
        ),
        migrations.AlterField(
            model_name="buildingworkperformedevent",
            name="work_performed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="buildings.buildingworkperformed",
                verbose_name="work performed",
            ),
        ),
        migrations.AlterField(
            model_name="statistic",
            name="consolidated_buildings",
            field=models.IntegerField(
                help_text="All the buildings that have been consolidated (risk category is 'consolidated')",
                null=True,
                verbose_name="consolidated buildings",
            ),
        ),
        migrations.AlterField(
            model_name="statistic",
            name="evaluated_buildings",
            field=models.IntegerField(
                help_text="All the approved buildings in the database",
                null=True,
                verbose_name="evaluated buildings",
            ),
        ),
        migrations.AlterField(
            model_name="statistic",
            name="people_under_risk",
            field=models.IntegerField(
                help_text="The number of people (residents count) living in RS1 risk buildings",
                null=True,
                verbose_name="people under risk",
            ),
        ),
    ]
