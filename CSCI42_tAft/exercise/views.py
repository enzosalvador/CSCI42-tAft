from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import *
from .forms import *

# Create your views here.
class ExerciseDetailsView(DetailView):
    model = ExerciseModel
    template_name = 'exercise/exercise-details.html'

class AddExerciseView(CreateView):
    model = ExerciseModel
    form_class = ExerciseModelForm
    template_name = 'exercise/exercise-add.html'

class EditExerciseView(UpdateView):
    model = ExerciseModel
    form_class = ExerciseModelForm
    template_name = 'exercise/exercise-edit.html'

def index(request):
    exercises = ExerciseModel.objects.all()
    context = {
        'exercises': exercises
    }
    return render(request, 'exercise/exercise.html', context)

