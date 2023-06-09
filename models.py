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
