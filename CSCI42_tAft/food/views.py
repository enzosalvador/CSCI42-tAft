from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import *
from .forms import *

# Model Views
class FoodDetailsView(DetailView):
    model = FoodModel
    template_name = 'food/food-details.html'


class AddFoodView(CreateView):
    model = FoodModel
    form_class = FoodForm
    template_name = 'food/food-add.html'


class EditFoodView(UpdateView):
    model = FoodModel
    form_class = FoodForm
    template_name = 'food/food-edit.html'

def index(request):
    foods = FoodModel.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'food/food.html', context)