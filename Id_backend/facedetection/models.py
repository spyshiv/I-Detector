from django.db import models

# Create your models here.
class Imagedata(models.Model):
	model_pic = models.ImageField(upload_to ='./upload', default = 'static/None/no-img.jpg')
	def imageLink(self):
		if self.model_pic:
			return '<a href="' + str(self.model_pic.url) + '">' + 'NameOfmodel_picGoesHere' + '</a>'
		else:
			return '<a href="''"></a>'
	imageLink.allow_tags = True
	imageLink.short_description = "model_pic Link"