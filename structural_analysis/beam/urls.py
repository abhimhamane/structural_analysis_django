from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='beam-landing'),
    path('create/', views.create_beam, name='beam-create'),
]