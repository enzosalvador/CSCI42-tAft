from django.db import models
from django.urls import reverse


#Food Model
class FoodModel(models.Model):
    food_id = models.IntegerField(primary_key=True, null=False)
    food_name = models.CharField(max_length = 25)
    calories_per_serving = models.IntegerField()
    protein_per_serving = models.IntegerField()
    fat_per_serving = models.IntegerField()
    carbs_per_serving = models.IntegerField()

    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return reverse('food:food-item', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('food:food-edit', kwargs={'pk': self.pk})



