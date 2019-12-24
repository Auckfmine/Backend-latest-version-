from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    c = (('temps complet', 'Temp Complet'), ('temps partiel', 'Temps Partiel'))
    group_choices = (('petite-section', 'Petite-Section'), ('moyenne-section', 'Moyenne-Section'), ('Creche', 'Creche'))
    # coté parent
    parent = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    student_first_name = models.CharField(max_length=20)
    student_last_name = models.CharField(max_length=20)
    student_sexe = models.CharField(max_length=25)
    nationality = models.CharField(max_length=20)
    student_birthday = models.CharField(max_length=20)
    father_name = models.CharField(max_length=25)
    father_profession = models.CharField(max_length=25)
    father_phone_number = models.CharField(max_length=25)
    mother_name = models.CharField(max_length=20)
    mother_profession = models.CharField(max_length=25)
    mother_phone_number = models.CharField(max_length=25)
    complete_adress = models.CharField(max_length=100)
    tlf_fix_number = models.CharField(max_length=30)
    img= models.ImageField(blank=True,null=True, default="images/profile-2398782_960_720_ZjcWbXL.png")    
    #img = models.ImageField(upload_to='images/',null=True,blank=True ,default="/images/profile-2398782_960_720_ZjcWbXL.png")

    # coté admin
    
    photo_1 = models.ImageField(blank = True,null = True,upload_to = 'images/')
    photo_2 = models.ImageField(blank = True,null = True ,upload_to = 'images/')
    photo_3 = models.ImageField(blank = True,null = True,upload_to = 'iamges/')
    
    photo_4 = models.ImageField(blank = True,null = True,upload_to = 'images/')
    photo_5 = models.ImageField(blank = True,null = True,upload_to = 'images/')
    photo_6 = models.ImageField(blank = True,null = True,upload_to = 'images/')
    
    
    section = models.CharField(max_length=25, choices=group_choices)
    nom_du_pediatre = models.CharField(null=True,blank=True,max_length=25)
    tlf_pediatre = models.CharField(null=True,blank=True,max_length=25)
    other_responsible_name = models.CharField(null=True,blank=True,max_length=25)
    other_responsible_tlf = models.CharField(null=True,blank=True,max_length=25)
    is_alergetic = models.CharField(max_length=25)
   
    
    
    auto_medic_buy = models.CharField(max_length=25)
    study_forfait = models.CharField(max_length=25, choices=c)
    def __str__(self):
        return self.student_first_name+" "+self.student_last_name
