from django.urls import path
from .views import *

appname="timetable"
urlpatterns = [
  path("", index, name="index")
]