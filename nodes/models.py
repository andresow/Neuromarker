from django.db import models
from django.contrib.auth.models import User
import datetime

class Nodes(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    is_red = models.BooleanField(default=True)
    name  = models.TextField(max_length=500, blank=True)
    percentage_commission = models.IntegerField()

class Node_father(models.Model):
    
    node =  models.OneToOneField(Nodes, primary_key=True, on_delete=models.CASCADE)
    initial_date = models.DateField(("Date"), default=datetime.date.today)
    final_date = models.DateField(null=True)

    def save_data(self,node):
        newNodoFather = Node_father(node=node)
        newNodoFather.save()

class Comission(models.Model):

    node = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    value_commision = models.IntegerField()
    type_payment = models.TextField(max_length=500, blank=True)
    type_commission = models.TextField(max_length=500, blank=True)
    current_balance = models.IntegerField(null=True)
