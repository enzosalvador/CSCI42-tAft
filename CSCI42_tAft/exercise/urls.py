from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('exercise/add/', AddExerciseView.as_view(), name='exercise-add'),
    path('exercise/<int:pk>/edit/', EditExerciseView.as_view(), name='exercise-edit'),
    path('exercise/<int:pk>/details/', ExerciseDetailsView.as_view(), name='exercise-item'),
]

app_name = "exercise"