from accounts.models import Account
from django.db import models
from django.contrib.auth import get_user_model
from renting_bike.models import Bikes

# User = get_user_model()




class Rent(models.Model):
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE,null="True")
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_time = models.IntegerField(null="True")
    total_cost = models.IntegerField()
    

