from django.contrib import admin
from .models import Imagedata

# Register your models here.
admin.site.register(Imagedata)

class FileAdmin(admin.ModelAdmin):
    list_display = ['imageLink']
    readonly_fields = ['imageLink']