# Generated by Django 4.1.2 on 2024-04-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_houseplant_statistic_statisticid_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='houseplant',
            index=models.Index(fields=['scientfic_name'], name='houseplant_scientf_f4db7d_idx'),
        ),
    ]
