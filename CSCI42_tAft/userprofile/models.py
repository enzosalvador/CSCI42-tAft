from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# User Profile Model
class UserProfileModel(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length = 50, default = "")
    last_name = models.CharField(max_length = 50, default = "")
    email = models.CharField(max_length = 50, default = "")
    height = models.DecimalField(max_digits=5, decimal_places=2, default = "Height")
    weight = models.DecimalField(max_digits=5, decimal_places=2, default = "Weight")

    def __str__(self):
         return self.first_name
    
    def get_absolute_url(self):
        return reverse('userprofile:userprofile-details', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('userprofile:userprofile-edit', kwargs={'pk': self.pk})