from django.db import models

# Create your models here.
class Imagedata(models.Model):
	upload_path = 'static/images/upload/'
	model_pic = models.ImageField(upload_to = upload_path, default = 'static/None/no-img.jpg')