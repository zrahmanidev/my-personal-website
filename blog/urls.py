from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListview.as_view(), name='blog_page'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='blog_post')
]
