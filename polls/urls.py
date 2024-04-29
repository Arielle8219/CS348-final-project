from django.urls import path

from . import views

urlpatterns = [
    path("", views.addPlant, name="addPlant"),
    path("getPlant", views.getPlant, name="getPlant"),
    path("removePlant", views.removePlant, name="removePlant"),
    path("updatePlant", views.updatePlant, name="updatePlant"),
    path("searchPlants", views.allCategoriesStatisticsCares, name="searchPlants"),
    path("addEasy", views.addEasy, name="addEasy"),
    path("addProblematic", views.addProblematic, name="addProblematic"),
    path("addExpensive", views.addExpensive, name="addExpensive"),
]