from django.contrib import admin
from django.urls import path,include
from blogapp import views

urlpatterns = [
     path('', views.home, name='home'),
     path('addpost/', views.addpost, name='addpost'),
     path('singlepost/<slug:url>', views.singlepost, name='singlepost'),
     path('delete_post/<id>',views.delete_post,name='delete_post'),
]