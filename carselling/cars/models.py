from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Car(models.Model):
    category = models.ForeignKey(Category,related_name='cars',on_delete=models.CASCADE)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=255, default='Not Specified')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='cars_images',blank=True,null=True)
    engine = models.CharField(max_length=255, default='Not Specified')
    transmission_type = models.CharField(max_length=255)
    is_sold = models.BooleanField(default=False)
    mileage = models.CharField(max_length=255,default='Not Specified')
    color = models.CharField(max_length=255, default='Not Specified')
    seller = models.ForeignKey(User,related_name='cars',on_delete=models.CASCADE)

    def __str__(self):
        return self.year+" "+self.make+" "+self.model