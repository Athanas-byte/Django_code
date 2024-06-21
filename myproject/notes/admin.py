from django.contrib import admin
from . import models

class NotesAdmin (admin.ModelAdmin):
    list_display = ['tittle',]


admin.site.register(models.Notes, NotesAdmin)
