from django.urls import path, include
from . import views

app_name = 'comment'
urlpatterns = [
    path('clist/', views.clist, name='clist'),
    path('cwrite/', views.cwrite, name='cwrite'),
]