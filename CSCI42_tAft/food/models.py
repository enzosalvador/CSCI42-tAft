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

class FoodConsumed(models.Model):
    user_food = models.IntegerField(primary_key=True, null=False)
    model = models.ForeignKey(
        'signup.UserModel',
        on_delete=models.RESTRICT,
        null=False)
    model = models.ForeignKey(
        FoodModel,
        on_delete=models.RESTRICT,
        null=False)
    servings = models.IntegerField()
    consumed_date = models.DateTimeField()

    def __str__(self):
        return self.user_food
