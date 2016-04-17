from django.conf import settings
from django.shortcuts import render
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

def face_extract(request):
	return render(request, 'face/face_extract.html')