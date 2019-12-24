from django.db import models
from student.models import Student


class Absence(models.Model):
    
    
    
    
    
    enfant = models.ForeignKey(Student,on_delete=models.CASCADE,)
    absence = models.BooleanField(default = False)
    date = models.DateField()


# Create your models here.
