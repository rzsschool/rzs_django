from django.urls import path, include
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('blog/<int:pk>', views.blog_detail, name='blog_detail'),
]
