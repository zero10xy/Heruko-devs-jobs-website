from django.urls import path

from . import views

urlpatterns = [
    path('job_listing', views.index, name='index'),
]