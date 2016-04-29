from django.conf import settings
from django.shortcuts import render
from facedetection.models import ImageData, imageModel
from django.template import RequestContext
from django.shortcuts import render_to_response

from .forms import imageModelForm
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
	if request.method == "GET":
		form = imageModelForm()
	else:
		form = imageModelForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	latest_image = imageModel.objects.all()
	for image in latest_image:
		subject_name = image.subject_name
		subject_id = image.subject_id
		Phone = image.phone_number
		Father = image.father_name
		Father_number = image.father_number
		Best_friend = image.best_friend
		Best_friend_number = image.best_friend_number
		subject_pic = image.subject_pic.url
	variables = RequestContext(request,{
	    'subject_name' :subject_name,
	    'subject_id' : subject_id,
	    'phone' : Phone ,
	    'father_name' : Father ,
	    'father_number' : Father_number ,
	    'best_friend' : Best_friend ,
	    'best_friend_number' : Best_friend_number,
	    'subject_pic' : subject_pic
	})

	return render(request, 'face/face_recog.html', {'form':form,'success_msg':"data is saved successfully",},variables)

# def face_extract(request):
# 	return render(request, 'face/face_extract.html')


def face_extract(request):
	images = ImageData.objects.all()
	for image in images:
		Name = image.name
		Phone = image.phone_number
		Father = image.father_name
		Father_number = image.father_number
		Best_friend = image.best_friend
		Best_friend_number = image.best_friend_number
		Images = image.model_pic.url
	variables = RequestContext(request,{
	    'name' : Name,
	    'phone' : Phone ,
	    'father_name' : Father ,
	    'father_number' : Father_number ,
	    'best_friend' : Best_friend ,
	    'best_friend_number' : Best_friend_number,
	    'images' : Images
	})
	return render_to_response('face/face_extract.html',variables)