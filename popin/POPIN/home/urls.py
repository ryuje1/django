from django.urls import path, include
from . import views

app_name = ''
urlpatterns = [
    path('', views.index, name="index"),
    path('landing/', views.landing, name="landing"),
]
