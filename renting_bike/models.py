from django.db import models
from django.db.models.signals import pre_save
from bike_rental.util import unique_slug_generator


# Create your models here.
class Bikes(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(max_length=200,null=True,blank=True)


def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=Bikes)
