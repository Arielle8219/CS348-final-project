# Generated by Django 4.1.2 on 2024-03-19 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Care',
            fields=[
                ('careID', models.CharField(help_text='Enter the care ID', max_length=20, primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='Enter a brief description of the care')),
            ],
            options={
                'db_table': 'care',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoryID', models.CharField(help_text='Enter the category ID', max_length=20, primary_key=True, serialize=False)),
                ('description', models.TextField(help_text='Enter a brief description of the category')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='HousePlant',
            fields=[
                ('scientfic_name', models.CharField(help_text='Enter the scientific name of the plant', max_length=20, primary_key=True, serialize=False)),
                ('common_name', models.CharField(max_length=20)),
                ('description', models.TextField(help_text='Enter a brief description of the plant')),
                ('idealGrowingConditions', models.TextField(help_text='Enter the ideal growing conditions for the plant')),
                ('imageURL', models.URLField(help_text='Enter the URL of the plant image')),
                ('careID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.care')),
            ],
            options={
                'db_table': 'houseplant',
            },
        ),
        migrations.CreateModel(
            name='PlantCategories',
            fields=[
                ('plant_category_id', models.CharField(help_text='Enter the plant category ID', max_length=20, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.categories')),
                ('scientific_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.houseplant')),
            ],
            options={
                'db_table': 'plantcategories',
            },
        ),
    ]