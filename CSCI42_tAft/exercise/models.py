from django.db import models
from django.urls import reverse
# Exercise Model
class ExerciseModel(models.Model):
    exercise_id = models.IntegerField(primary_key=True, null=False)
    exercise_name = models.CharField(max_length = 25)
    calories_burned_per_hour = models.IntegerField()

    def __str__(self):
            return self.exercise_name

 
