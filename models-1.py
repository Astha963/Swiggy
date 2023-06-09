from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=20,null = True,blank = True)
    lastname = models.TextField(max_length=20,null = True,blank = True)
    birth = models.DateField(max_length=20,null = True,blank = True)
    mobile = models.IntegerField(max_length=20,null = True,blank = True)
    GENDER_TYPE = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    gender = models.IntegerField(
        choices=GENDER_TYPE,
        default=1
    )
class Orders(models.Model):
    order_name = models.CharField(max_length=20,null = True,blank = True)
    order_price = models.CharField(max_length=20,null = True,blank = True)
    order_discount = models.CharField(max_length=20,null = True,blank = True)
    order_quality = models.CharField(max_length=20,null = True,blank = True)
    order_address = models.CharField(max_length=20,null = True,blank = True)
    order_place_at = models.CharField(max_length=20,null = True,blank = True)
    