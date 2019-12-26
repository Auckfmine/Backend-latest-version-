from django.db import models
from student.models import Student



class date(models.Model):
    date = models.DateField(auto_now_add= False)

    

    child = models.ForeignKey(Student,null=True,blank=True,on_delete  = models.CASCADE)

    data1 = models.CharField(null=True,blank=True,max_length=255)
# Create your models here.
