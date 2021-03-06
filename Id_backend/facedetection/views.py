from django.conf import settings
from django.shortcuts import render
from facedetection.models import ImageData, imageModel
from django.template import RequestContext
from django.shortcuts import render_to_response

from .forms import imageModelForm, ImageDataForm
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
	latest_image = imageModel.objects.all()
	custom = imageModel.objects.get(subject_id="baran")
	print "##############", custom.phone_number
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
	return render_to_response('face/face_extract.html',variables)

def face_search(request):
	if request.method == "GET":
		form = ImageDataForm()
	else:
		form = ImageDataForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	uploaded_image = ImageData.objects.all()
	for image in uploaded_image:
		image_url = image.model_pic.url
	variables = RequestContext(request,{
		'image_for_search' : image_url
		})
	return render_to_response('face/face_search.html',{'form':form,'success_msg':"data is saved successfully",}, variables)

