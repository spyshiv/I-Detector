from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about-us', views.about_us, name='about_us'),
    url(r'^contact-us', views.contact_us, name='contact_us'),
    url(r'^references', views.references, name='references'),

    #projects parts
    url(r'^face-detect', views.face_detect, name='face_detect'),
    url(r'^face-recog', views.face_recog, name='face_recog'),
    url(r'^face-extract', views.face_extract, name='face_extract'),
]
