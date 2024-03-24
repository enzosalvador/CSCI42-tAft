from django.db import models

# Create your models here.
class UserModel(models.Model):
    #username for login 
    user_id = models.CharField(max_length=10, primary_key=True, null=False)

    #password for login
    password = models.CharField(max_length = 50)

    #user details
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.CharField(max_length = 50)
    age = models.IntegerField()
    height =  models.IntegerField()
    weight = models.IntegerField()


    def __str__(self):
        return self.user_id