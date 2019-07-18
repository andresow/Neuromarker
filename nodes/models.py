from django.db import models

class Nodes(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_red = models.BooleanField()
    name  = models.TextField(max_length=500, blank=True)
    percentage_commission = models.IntegerField()

class Node_father(models.Model):
    
    node =  models.OneToOneField(Nodes, primary_key=True)
    initial_date = models.DateField()
    final_date = models.DateField()

class Comission(models.Model):

    node = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    value_commision = models.IntegerField()
    type_payment = models.TextField(max_length=500, blank=True)
    type_commission = models.TextField(max_length=500, blank=True)
    current_balance = models.IntegerField(null=True)
