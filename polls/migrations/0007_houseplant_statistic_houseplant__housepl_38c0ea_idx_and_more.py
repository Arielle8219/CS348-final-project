# Generated by Django 4.1.2 on 2024-04-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_care_care_careid_ecfa5d_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='houseplant_statistic',
            index=models.Index(fields=['HousePlantID'], name='houseplant__HousePl_38c0ea_idx'),
        ),
        migrations.AddIndex(
            model_name='plantcategories',
            index=models.Index(fields=['scientific_name'], name='plantcatego_scienti_00b9ae_idx'),
        ),
    ]
