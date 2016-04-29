from django.db import models

# Create your models here.
class ImageData(models.Model):
	name = models.CharField(max_length=200,  blank=True)
	phone_number = models.CharField(max_length=200,  blank=True)
	father_name = models.CharField(max_length=200,  blank=True)
	father_number = models.CharField(max_length=200,  blank=True)
	best_friend = models.CharField(max_length=200,  blank=True)
	best_friend_number = models.CharField(max_length=200,  blank=True)
	model_pic = models.ImageField(upload_to ='./upload', default = 'static/None/no-img.jpg')
	

class imageModel(models.Model):
	subject_name = models.CharField(max_length=200, blank=True)
	subject_id = models.CharField(max_length=200, blank=True)
	phone_number = models.CharField(max_length=200,  blank=True)
	father_name = models.CharField(max_length=200,  blank=True)
	father_number = models.CharField(max_length=200,  blank=True)
	best_friend = models.CharField(max_length=200,  blank=True)
	best_friend_number = models.CharField(max_length=200,  blank=True)
	subject_pic = models.ImageField(upload_to="./upload/imagedb")
