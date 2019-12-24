from django.contrib import admin
from .models import Rv
# Register your models here.

class Rv_admin(admin.ModelAdmin):
    list_display = ['Rv_user','Rv_available_date','date']
admin.site.register(Rv,Rv_admin)
