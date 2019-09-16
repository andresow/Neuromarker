from django.db import models
from django.contrib.auth.models import User
import datetime

class Nodes(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    is_red = models.BooleanField(default=True)
    name  = models.TextField(max_length=500, blank=True)
    saldo = models.IntegerField()
    percentage_commission = models.IntegerField()
    id_father = models.IntegerField(null=True)

    def save_data(self,is_red,user,id_father,name,percentage_commission):
        newNodo = Node(user=user,is_red=is_red, name=name,percentage_commission=percentage_commission,id_father=id_father)
        newNodo.save()

class Node_father(models.Model):
    
    node =  models.ForeignKey(Nodes, unique=True, primary_key=True, on_delete=models.CASCADE)
    initial_date = models.DateField(("Date"), default=datetime.date.today)
    final_date = models.DateField(null=True)
    generateCode =  models.TextField(max_length=500, blank=True)

    def save_data(self,node,generateCode):
        newNodoFather = Node_father(node=node, generateCode=generateCode)
        newNodoFather.save()

class Comission(models.Model):

    node = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    value_commision = models.IntegerField()
    type_payment = models.TextField(max_length=500, blank=True)
    type_commission = models.TextField(max_length=500, blank=True)
    current_balance = models.IntegerField(null=True)

    def save_data(self,node,generateCode):
        newComission = Comission(value_commision=value_commision, type_payment=type_payment, type_commission=type_commission, current_balance=current_balance,node=node)
        newComission.save()
