from django.contrib import admin
from .models import Notes
class NotesAdmin(admin.ModelAdmin):
    list_display = ['student','title']
    search_fields = ['student','title']

admin.site.register(Notes,NotesAdmin)
