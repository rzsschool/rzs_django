from django.urls import path

from . import views

urlpatterns = [
    path('page/<slug:relative_link>', views.page, name="index")
]
