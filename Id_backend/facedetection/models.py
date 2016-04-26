from django.db import models

# Create your models here.
class Imagedata(models.Model):
	name = models.CharField(max_length=200,  blank=True)
	phone_number = models.CharField(max_length=200,  blank=True)
	father_name = models.CharField(max_length=200,  blank=True)
	father_number = models.CharField(max_length=200,  blank=True)
	best_friend = models.CharField(max_length=200,  blank=True)
	best_friend_number = models.CharField(max_length=200,  blank=True)
	model_pic = models.ImageField(upload_to ='./upload', default = 'static/None/no-img.jpg')
	def imageLink(self):
		if self.model_pic:
			return '<a href="' + str(self.model_pic.url) + '">' + 'NameOfmodel_picGoesHere' + '</a>'
		else:
			return '<a href="''"></a>'
	imageLink.allow_tags = True
	imageLink.short_description = "model_pic Link"