from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    # views.py로 연결
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]