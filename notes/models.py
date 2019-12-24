from django.db import models
from student.models import Student

class Notes(models.Model):

    
    c = (('1', '1'), ('2', '2'),('3','3'))



    student  = models.ForeignKey(Student,on_delete = models.CASCADE)
    
    title = models.CharField(max_length=50,default=" ")
    Attitude_En_Classe = models.CharField(max_length=25, choices=c,null=True)
    Respect_Des_Consignes = models.CharField(max_length=25, choices=c,null=True)
    Autonomie = models.CharField(max_length=25, choices=c,null=True)
    Sociabilite = models.CharField(max_length=25, choices=c,null=True)
    Concentration = models.CharField(max_length=25, choices=c,null=True)
    
    Proprete= models.CharField(max_length=25, choices=c,null=True)
    def __str__(self):
        return str(self.student.student_first_name+" "+self.student.student_last_name)


