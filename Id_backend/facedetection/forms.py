from django import forms
from .models import imageModel

class imageModelForm(forms.ModelForm):
	class Meta:
		model = imageModel
		fields ="__all__"