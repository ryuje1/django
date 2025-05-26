from django.urls import path, include
from . import views

urlpatterns = [
    path('member/', views.member, name='member'),
]
