from django.db import models

# Create your models here.
class Imagedata(models.Model):
	upload_path = 'media/faces'
	model_pic = models.ImageField(upload_to = upload_path, default = 'pic_folder/None/no-img.jpg')