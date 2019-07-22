from django.db import models
from nodes.models import Nodes, Node_father

class Product(models.Model):

    node = models.ForeignKey(Node_father, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    value = models. IntegerField()
    quantity = models.IntegerField()
    restriction = models.BooleanField()
    state = models.CharField(max_length=20)
    category = models.CharField(max_length=200)
    picture = models.ImageField(null=True)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(str(self.id) + self.name)

    def lastProductId(self):
        return str(Product.objects.latest('id'))

class Image(models.Model):
    filename = models.CharField(max_length=100)
    docfile = models.ImageField(upload_to='static/images/')
        
    def __unicode__(self):
        return '%s' % (self.nombre)

 