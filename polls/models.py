from django.db import models
from django.urls import reverse

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field


class HousePlant (models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    scientfic_name = models.CharField(max_length=20, primary_key=True, help_text='Enter the scientific name of the plant')
    common_name = models.CharField(max_length=20)
    description = models.TextField(help_text='Enter a brief description of the plant')
    careID = models.ForeignKey('Care', on_delete=models.SET_NULL, null=True)
    idealGrowingConditions = models.TextField(help_text='Enter the ideal growing conditions for the plant')
    imageURL = models.URLField(max_length=200, help_text='Enter the URL of the plant image')
    
    class Meta:
        db_table = 'houseplant'
        indexes = [
            models.Index(fields = ['scientfic_name'])
        ]
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.common_name
    
class Care (models.Model):
    careID = models.CharField(max_length=20, primary_key=True, help_text='Enter the care ID')
    description = models.TextField(help_text='Enter a brief description of the care')
    
    class Meta:
        db_table = 'care'
        indexes = [
            models.Index(fields = ['careID'])
        ]
    def __str__(self) -> str:
        return self.description

class Categories (models.Model):
    categoryID = models.CharField(max_length=20, primary_key=True, help_text='Enter the category ID')
    name = models.CharField(max_length=20, help_text='Enter the name of the category', default = "")
    description = models.TextField(help_text='Enter a brief description of the category')

    class Meta:
        db_table = 'categories'
    def __str__(self) -> str:
        return self.name
    
    
class PlantCategories(models.Model):
    plant_category_id = models.CharField(max_length=20, primary_key=True, help_text='Enter the plant category ID')
    scientific_name = models.ForeignKey('HousePlant', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Categories', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'plantcategories'
        indexes = [
            models.Index(fields = ['scientific_name'])
        ]


class HousePlant_Statistic(models.Model):
    """Model representing the relationship between HousePlant and Statistic."""
    HousePlant_StatisticID = models.AutoField(primary_key=True)
    HousePlantID = models.ForeignKey('HousePlant', on_delete=models.CASCADE)
    #StatisticID = models.ForeignKey('Statistics', on_delete=models.CASCADE)
    popularity = models.IntegerField(help_text='Votes for this plant being popular', default = 0)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter the price of the plant', default = 0)
    beginnerFriendly = models.IntegerField(help_text='Votes for this plant being beginner friendly', default = 0)
    searchCount = models.IntegerField(help_text='Enter the search count of the plant', default = 0)
    expensive = models.DecimalField(max_digits=10, decimal_places=2, help_text='Votes for this plant being expensive to care for', default = 0)
    problematic = models.DecimalField(max_digits=10, decimal_places=2, help_text='Votes for this plant being problematic to care for', default = 0)

    class Meta:
        db_table = 'houseplant_statistic'
        indexes = [
            models.Index(fields = ['HousePlantID'])
        ]

    def __str__(self):
        """String for representing the HousePlant_Statistic object."""
        return f'{self.HousePlantID} - {self.HousePlant_StatisticID}'
    

class Statistics(models.Model):
    """Model representing a statistic. NO longer used """
    statisticID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='Enter the name of the statistic')
    description = models.TextField(help_text='Enter a brief description of the statistic', default = "")
    class Meta:
        db_table = 'statistics'

    def __str__(self):
        """String for representing the Statistics object."""
        return self.name
