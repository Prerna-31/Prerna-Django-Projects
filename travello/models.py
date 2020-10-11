from django.db import models

# Create your models here.

#class destination:
 #   id    : int
  #  img   : str
   # name  : str
    #desc  : str
    #price : int
    #offer : bool
#Modified above class to use to create table(map to database)
class destination(models.Model):   ## Inherit models
    img = models.ImageField(upload_to='db_pics')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)