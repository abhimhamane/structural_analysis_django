from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='blog-landing'),
    path('about/', views.about, name='blog-about'),
    path('register/', views.get_name, name='create'),
]