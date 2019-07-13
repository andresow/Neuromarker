from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class Profile(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    birthday = models. DateField()
    address  = models.TextField(max_length=500, blank=True)
    
    def save_data(self,identification,userType,user):
        newProfile = Profile(birthday=birthday,address=address,user=user)
        newProfile.save()
        
        def __str__(self):
            return '{}'.format(self.identification)