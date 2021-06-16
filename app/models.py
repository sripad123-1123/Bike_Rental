from django.db import models
from django.contrib.auth import get_user_model
from renting_bike.models import Bikes

User = get_user_model()


# Create your models here.
# class Bikes(models.Model):
#     name = models.CharField(max_length=200)
#     img = models.ImageField(upload_to='pictures')
#     desc = models.TextField()
#     price = models.IntegerField()
    

# class MotorBike(models.Model):
#     name = models.CharField(max_length=200)
#     img = models.ImageField(upload_to='pictures')
#     desc = models.TextField()
#     price = models.IntegerField()


class Rent(models.Model):
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE,null="True")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_time = models.IntegerField(null="True")
    total_cost = models.IntegerField()
    

