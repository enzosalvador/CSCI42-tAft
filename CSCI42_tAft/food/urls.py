from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('food/add/', AddFoodView.as_view(), name='food-add'),
    path('food/<int:pk>/edit/', EditFoodView.as_view(), name='food-edit'),
    path('food/<int:pk>/details/', FoodDetailsView.as_view(), name='food-item'),
]

app_name = "food"