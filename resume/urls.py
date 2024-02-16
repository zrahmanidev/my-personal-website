from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_resume, name='resume_page')
]
