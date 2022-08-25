from django.urls import path

from . import views

urlpatterns = [
    path('staff', views.staff, name='staff'),
    path('staff/<int:pk>', views.staff_detail, name='staff_detail'),
]
