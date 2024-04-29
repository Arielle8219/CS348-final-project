# Generated by Django 4.1.2 on 2024-04-22 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('statisticID', models.AutoField(primary_key=True, serialize=False)),
                ('statistic_name', models.CharField(help_text='Enter the name of the statistic', max_length=100)),
            ],
            options={
                'db_table': 'statistics',
            },
        ),
        migrations.CreateModel(
            name='HousePlant_Statistic',
            fields=[
                ('HousePlant_StatisticID', models.AutoField(primary_key=True, serialize=False)),
                ('HousePlantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.houseplant')),
                ('StatisticID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.statistics')),
            ],
            options={
                'db_table': 'houseplant_statistic',
            },
        ),
    ]