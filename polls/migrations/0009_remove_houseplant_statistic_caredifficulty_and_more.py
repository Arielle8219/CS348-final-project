# Generated by Django 4.1.2 on 2024-04-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_houseplant_statistic_searchcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseplant_statistic',
            name='careDifficulty',
        ),
        migrations.AddField(
            model_name='houseplant_statistic',
            name='beginnerFriendly',
            field=models.IntegerField(default=0, help_text='Votes for this plant being beginner friendly'),
        ),
        migrations.AddField(
            model_name='houseplant_statistic',
            name='expensive',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Votes for this plant being expensive to care for', max_digits=10),
        ),
        migrations.AddField(
            model_name='houseplant_statistic',
            name='problematic',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Votes for this plant being problematic to care for', max_digits=10),
        ),
    ]