from polls.models import HousePlant, Care, Categories, PlantCategories

def creation():
    H1 = Care(careID = "H1", description = "Watering")
    H1.save()
    hydrangea = HousePlant(scientific_name = "Hydrangea", 
                        common_name = "Hydrangea", 
                        description = "Flowering shrubs that are natural pH indicators", 
                        careID = "H1", 
                        idealGrowingConditions = "Partial sun, moist soil", 
                        imageURL = "https://en.wikipedia.org/wiki/Hydrangea#/media/File:Bauernhortensie_Wochenmarkt.jpg")

    hydrangea.save()