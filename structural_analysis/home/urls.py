from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.HomeView, name='index'),
    path('sympy_workflow/', views.sympyIpy, name='sympy_workflow'),
]