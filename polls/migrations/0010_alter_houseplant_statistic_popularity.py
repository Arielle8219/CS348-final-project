# Generated by Django 4.1.2 on 2024-04-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_houseplant_statistic_caredifficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseplant_statistic',
            name='popularity',
            field=models.IntegerField(default=0, help_text='Votes for this plant being popular'),
        ),
    ]