from django.contrib import admin
from .models import ImageData, imageModel

# Register your models here.
admin.site.register(ImageData)
admin.site.register(imageModel);

class FileAdmin(admin.ModelAdmin):
    list_display = ['imageLink']
    readonly_fields = ['imageLink']