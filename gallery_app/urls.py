from django.urls import path
from gallery_app import views

urlpatterns = [

    path('',views.gallery,name='gallery'),
    path('gallerydetail/<int:id>',views.gallery_detail,name='gallery_detail'),

]