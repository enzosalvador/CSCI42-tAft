from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import *
from .forms import *

from django.shortcuts import redirect
from .models import UserProfileModel

class UserDetailsView(DetailView):
    model = UserProfileModel
    template_name = 'userprofile/userprofile-details.html'

class AddUserProfileView(CreateView):
    model = UserProfileModel
    form_class = UserProfileForm
    template_name = 'userprofile/userprofile-add.html'

class EditUserProfileView(UpdateView):
    model = UserProfileModel
    form_class = UserProfileForm
    template_name = 'userprofile/userprofile-edit.html'

def index(request):
    userprofiles = UserProfileModel.objects.all()
    context = {
        'userprofiles': userprofiles
    }
    return render(request, 'userprofile/userprofile.html', context)