from django.db import models

# Create your models here.
class ExerciseModel(models.Model):
    exercise_id = models.IntegerField(primary_key=True, null=False)
    exercise_name = models.CharField(max_length = 25)
    duration = models.IntegerField()
    calories_burned_per_hour = models.IntegerField()

    def __str__(self):
            return self.exercise_id
    
