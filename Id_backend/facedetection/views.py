from django.conf import settings
from django.shortcuts import render
from facedetection.models import Imagedata
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    return render(request, 'index.html', {"static_url": settings.STATIC_URL})


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def references(request):
    return render(request, 'references.html')


#Project parts
def face_detect(request):
	return render(request, 'face/face_detect.html')


def face_recog(request):
	return render(request, 'face/face_recog.html')

# def face_extract(request):
# 	return render(request, 'face/face_extract.html')


def face_extract(request):
	images = Imagedata.objects.all()
	for image in images:
	    Images = image.model_pic.url
	variables = RequestContext(request,{
	    'images':Images
	})
	return render_to_response('face/face_extract.html',variables)