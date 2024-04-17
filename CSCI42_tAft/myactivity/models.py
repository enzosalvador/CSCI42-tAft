# from django.db import models
# from django.urls import reverse
# from food.models import FoodModel
# from exercise.models import ExerciseModel

# class FoodConsumed(models.Model):
#     user_food = models.IntegerField(primary_key=True, null=False)
#     model = models.ForeignKey(
#         UserModel,
#         on_delete=models.RESTRICT,
#         null=False)
#     model = models.ForeignKey(
#         FoodModel,
#         on_delete=models.RESTRICT,
#         null=False)
#     servings = models.IntegerField()
#     consumed_date = models.DateTimeField()

#     def __str__(self):
#         return self.user_food
    
# #Exercise Done Model
# class ExerciseDone(models.Model):
#     user_exercise = models.IntegerField(primary_key=True, null=False)
#     model = models.ForeignKey(
#         UserModel,
#         on_delete=models.RESTRICT,
#         null=False)
#     model = models.ForeignKey(
#         ExerciseModel,
#         on_delete=models.RESTRICT,
#         null=False)
#     duration = models.IntegerField()
#     workout_date = models.DateTimeField()

#     def __str__(self):
#         return self.user_exercise
