from django.urls import path
from . import views
urlpatterns=[
    path("" ,views.index,name="index"),
    path("post" ,views.details,name="details"),
    path("clear" ,views.screen,name="screen")
]