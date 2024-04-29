from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple
from polls.models import HousePlant, Care, Categories, PlantCategories, HousePlant_Statistic, Statistics

Cares = namedtuple('Cares', ['careID', 'description'])
Category = namedtuple('Categories', ['categoryID', 'name', 'description'])
PlantCategory = namedtuple('PlantCategories', ['plant_category_id', 'scientific_name', 'category'])
HousePlant_Statistics = namedtuple('HousePlant_Statistic', ['HousePlant_StatisticID', 'HousePlantID', 'popularity', 'price', 'beginnerFriendly', 'searchCount', 'expensive', 'problematic'])
HousePlants = namedtuple('HousePlant', ['scientfic_name', 'common_name', 'description', 'careID', 'idealGrowingConditions', 'imageURL'])





def getPlant(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM houseplant"
        )
        plants = [HousePlants(*row) for row in cursor.fetchall()]
    return render(request, 'viewPlant.html', {'plants': plants})
def removePlant(request):
    if request.method == "POST":
        scientific_name = request.POST.get('scientific_name')
        row_to_delete = HousePlant.objects.get(scientfic_name=scientific_name)
        row_to_delete.delete()
        return HttpResponse("Successfully deleted")
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM houseplant"
            )
            plants = [HousePlants(*row) for row in cursor.fetchall()]
        return render(request, 'removePlant.html', {'plants': plants})

def updatePlant(request):
    if request.method == "POST":
        scientific_name = request.POST.get('scientific_name')
        plant = HousePlant.objects.get(scientfic_name=scientific_name)
        field_name = request.POST.get('field_name')
        new_value = request.POST.get('new_value')
        if (field_name == "careID"):
            try:
                careObj = Care.objects.get(careId = new_value)
            except Care.DoesNotExist:
                return HttpResponse("Care object does not exist")
            setattr(plant, field_name, careObj)
        else:
            setattr(plant, field_name, new_value)
        plant.save()
        return HttpResponse("Successfully updated")
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM houseplant"
            )
            plants = [HousePlants(*row) for row in cursor.fetchall()]
        return render(request, 'removePlant.html', {'plants': plants})

def addPlant(request):
    # creation()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM care"
        )
        care = [Cares(*row) for row in cursor.fetchall()]
    print(care)
    if request.method == "POST":

        scientific_name1 = request.POST.get('scientific_name')
        common_name1 = request.POST.get('common_name')
        description1 = request.POST.get('description')
        careID1 = request.POST.get('careID')
        idealGrowingConditions1 = request.POST.get('idealGrowingConditions')
        imageURL1 = request.POST.get('imageURL')
        
        try:
            with connection.cursor() as cursor:
                careObj = Care.objects.get(careID = careID1)
        except Care.DoesNotExist:
            return HttpResponse("Care object does not exist")
        # Do something with the data, such as saving it to a database
        houseplant = HousePlant(scientfic_name = scientific_name1, 
                                common_name = common_name1,
                                description = description1,
                                careID = careObj,
                                idealGrowingConditions = idealGrowingConditions1,
                                imageURL = imageURL1)
    
       
        houseplant.save()
        houseplant_statistic = HousePlant_Statistic(HousePlantID=houseplant)
        houseplant_statistic.save()
        print(houseplant)
        return HttpResponse("Form submitted successfully")
    else:
        return render(request, 'addPlant.html', {'care': care})

def allCategoriesStatisticsCares(request):
    if request.method == "POST":
        category_id = request.POST.get('categoryId')
        statistic_id = request.POST.get('statisticId')
        care_id = request.POST.get('careId')

        print("STUFF: ", category_id, statistic_id, care_id)
        plants = HousePlant.objects.all()

        if category_id and category_id != "ALL":
            plants = plants.filter(plantcategories__category=category_id)


        if care_id and care_id != "ALL":
            plants = plants.filter(careID=care_id)
        
        if statistic_id:
            if statistic_id == "popularity":
                plants = plants.order_by('-houseplant_statistic__searchCount')
            elif statistic_id == "beginnerFriendly":
                plants = plants.order_by('-houseplant_statistic__beginnerFriendly')
            elif statistic_id == "expensive": 
                plants = plants.order_by('-houseplant_statistic__expensive')
            elif statistic_id == "problematic":
                plants = plants.order_by('-houseplant_statistic__problematic')


        #map plant ids to matching categories and care tips
        categories = {}
        statistics = {}
        for plant in plants:
            try:
                tempCategory = PlantCategories.objects.get(scientific_name=plant.scientfic_name)
                categories[plant.scientfic_name] = tempCategory.category
            except PlantCategories.DoesNotExist:
                categories[plant.scientfic_name] = []
            try:
                tempStat = HousePlant_Statistic.objects.get(HousePlantID=plant.scientfic_name)
                statistics[plant.scientfic_name] = tempStat
                numSearches = tempStat.searchCount
                setattr(tempStat, 'searchCount', numSearches + 1)
                tempStat.save()
            except HousePlant_Statistic.DoesNotExist:
                statistics[plant.scientfic_name] = []
        print("CATEgories", categories)
        print("Statistics", statistics)
        context = {
            'plants': plants,
            'categories': categories,
            'statistics': statistics
        }
        print(context)
        return render(request, 'viewPlant.html', {'context': context})
    else:
        categories = Categories.objects.all()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM houseplant_statistic"
            )
            statistics = [HousePlant_Statistics(*row) for row in cursor.fetchall()]
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM care"
            )
            cares = [Cares(*row) for row in cursor.fetchall()]
        return render(request, 'search_plants.html', {'categories': categories, 'statistics': statistics, 'cares': cares})


def addStatistic(request):
    if request.method == "POST":
        plant_id = request.POST.get('plant_id')
        statistic_id = request.POST.get('statistic_id')

        try:
            plant = HousePlant.objects.get(id=plant_id)
        except HousePlant.DoesNotExist:
            return HttpResponse("Plant does not exist")

        try:
            statistic = Statistics.objects.get(id=statistic_id)
        except Statistics.DoesNotExist:
            return HttpResponse("Statistic does not exist")

        houseplant_statistic = HousePlant_Statistic(HousePlantID=plant, StatisticID=statistic)
        houseplant_statistic.save()

        return HttpResponse("Statistic added successfully")
    else:
        return render(request, 'addStatistic.html')

def addEasy(request):
    if request.method == "POST":
        plant_id = request.POST.get('plant')

        try:
            plant = HousePlant.objects.get(scientfic_name=plant_id)
        except HousePlant.DoesNotExist:
            return HttpResponse("Plant does not exist")

        houseplant_statistic = HousePlant_Statistic.objects.get(HousePlantID=plant)
        houseplant_statistic.beginnerFriendly += 1
        houseplant_statistic.save()
        return HttpResponse("Statistic added successfully")
    else:
        return None
def addProblematic(request):
    if request.method == "POST":
        plant_id = request.POST.get('plant')

        try:
            plant = HousePlant.objects.get(scientfic_name=plant_id)
        except HousePlant.DoesNotExist:
            return HttpResponse("Plant does not exist")

        houseplant_statistic = HousePlant_Statistic.objects.get(HousePlantID=plant)
        houseplant_statistic.problematic += 1
        houseplant_statistic.save()
        return HttpResponse("Statistic added successfully")
    else:
        return None
def addExpensive(request):
    if request.method == "POST":
        plant_id = request.POST.get('plant')

        try:
            plant = HousePlant.objects.get(scientfic_name=plant_id)
        except HousePlant.DoesNotExist:
            return HttpResponse("Plant does not exist")

        houseplant_statistic = HousePlant_Statistic.objects.get(HousePlantID=plant)
        houseplant_statistic.expensive += 1
        houseplant_statistic.save()
        return HttpResponse("Statistic added successfully")
    else:
        return None
def getStatisticsForPlant(request, plant_id):
    if request.method == "POST":
        try:
            plant = HousePlant.objects.get(id=plant_id)
        except HousePlant.DoesNotExist:
            return HttpResponse("Plant does not exist")

        statistics = HousePlant_Statistic.objects.filter(HousePlantID=plant)

        # You can customize the format of the response based on your requirements
        data = {
            'plant_id': plant_id,
            'statistics': [{'id': stat.StatisticID.id, 'name': stat.StatisticID.statistic_name} for stat in statistics]
        }
        return render(request, 'viewStatistics.html', {'data': data})
    else :

        return render(request, 'viewStatistics.html', {'data': data})
    