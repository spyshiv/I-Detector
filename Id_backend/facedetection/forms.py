from django import forms
from .models import ImageData , imageModel

class imageModelForm(forms.ModelForm):
	class Meta:
		model = imageModel
		fields ="__all__"

class ImageDataForm(forms.ModelForm):
	class Meta:
		model = ImageData
		fields ="__all__"