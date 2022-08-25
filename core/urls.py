from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/menu', views.get_json_menu, name="get_json_menu"),

]
