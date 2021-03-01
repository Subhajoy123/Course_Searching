from django.db import models

# Create your models here.
class course(models.Model):
    name= models.CharField(max_length=100)
    # id : int
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    link= models.TextField()
    price= models.IntegerField()
    