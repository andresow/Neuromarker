from django.db import models

class Nodes(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_red = models.BooleanField()
    name  = models.TextField(max_length=500, blank=True)

class Node_father(models.Model):
    
    node =  models.OneToOneField(Nodes, primary_key=True)
    initial_date = models.DateField()
    final_date = models.DateField()

