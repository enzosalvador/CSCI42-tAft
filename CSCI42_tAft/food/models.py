from django.db import models
from django.db import reverse


#Food Model
class FoodModel(models.Model):
    food_id = models.IntegerField(primary_key=True, null=False)
    food_name = models.CharField(max_length = 25)
    calories_per_serving = models.IntegerField()
    protein_per_serving = models.IntegerField()
    fat_per_serving = models.IntegerField()
    carbs_per_serving = models.IntegerField()

