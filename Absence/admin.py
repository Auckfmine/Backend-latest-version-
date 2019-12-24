from django.contrib import admin
from .models import Absence


class Absence_admin(admin.ModelAdmin):

    list_display = ['enfant','absence','date']
    search_fields = ['enfant','date']




admin.site.register(Absence,Absence_admin)


# Register your models here.
