from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=40)
    description = models.TextField()
    value = models. IntegerField()
    quantity = models.IntegerField()
    restriction = models.IntegerField(blank=True)
    state = models.CharField(max_length=20)
    
    def __str__(self):
        return '{}'.format(self.name)