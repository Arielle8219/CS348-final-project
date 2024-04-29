from django.contrib import admin

# Register your models here.

from .models import HousePlant, Care, Categories, PlantCategories, HousePlant_Statistic, Statistics

admin.site.register(HousePlant)
admin.site.register(Care)
admin.site.register(Categories)
admin.site.register(PlantCategories)
admin.site.register(HousePlant_Statistic)
admin.site.register(Statistics)
