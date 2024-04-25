from django.db import models
from django.urls import reverse
# Exercise Model
class ExerciseModel(models.Model):
    exercise_id = models.IntegerField(primary_key=True, null=False)
    exercise_name = models.CharField(max_length = 100)
    calories_burned_per_hour = models.IntegerField()

    def __str__(self):
        return self.exercise_name

    def get_absolute_url(self):
        return reverse('exercise:exercise-item', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('exercise:exercise-edit', kwargs={'pk': self.pk})
 
