from django.db import models

# Exercise Model
class ExerciseModel(models.Model):
    exercise_id = models.IntegerField(primary_key=True, null=False)
    exercise_name = models.CharField(max_length = 25)
    calories_burned_per_hour = models.IntegerField()

    def __str__(self):
            return self.exercise_id

 
#Exercise Done Model
class ExerciseDone(models.Model):
    user_exercise = models.IntegerField(primary_key=True, null=False)
    model = models.ForeignKey(
        'signup.UserModel',
        on_delete=models.RESTRICT,
        null=False)
    model = models.ForeignKey(
        ExerciseModel,
        on_delete=models.RESTRICT,
        null=False)
    duration = models.IntegerField()
    workout_date = models.DateTimeField()

    def __str__(self):
        return self.user_exercise