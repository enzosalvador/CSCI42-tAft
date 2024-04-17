from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('userprofile/add/', AddUserProfileView.as_view(), name='userprofile-add'),
    path('userprofile/<int:pk>/edit/', EditUserProfileView.as_view(), name='userprofile-edit'),
    path('userprofile/<int:pk>/details/', UserDetailsView.as_view(), name='userprofile-details'),
]

app_name = "userprofile"