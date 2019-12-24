from django.db import models


class Homepage(models.Model):
    group_choices = (('petite-section', 'Petite-Section'), ('moyenne-section', 'Moyenne-Section'), ('Creche', 'Creche'))
    theme = models.CharField(null=True,blank=True,default=" ",max_length=100)
    Planning = models.ImageField(blank=True,null=True,upload_to="planning/")
    planning_cantine = models.ImageField(null=True,upload_to="planning/",blank=True)
    planning_goute = models.ImageField(null = True,upload_to = "planning/",blank = True)
    citation = models.ImageField(null = True ,upload_to = "planning/",blank = True)
    
    
    message = models.TextField(blank=True,default=' ', null=True)
    daily_img = models.ImageField(upload_to="daily-img/", null=True,blank=True)
    group = models.CharField(max_length=250, choices=group_choices)
    Event_title = models.CharField(blank=True,null=True,default=" ",max_length=100)
    Event_description = models.TextField(null=True,blank=True,default=' ')
    Event_date = models.DateField(blank=True,null=True   )
    Event_img = models.ImageField(upload_to="events/", null=True,blank=True)


'''class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=' ')
    date = models.DateField()
    img = models.ImageField(upload_to="events/", null=True)
    #group= models.ForeignKey(Enfant,on_delete=models.CASCADE)
'''
