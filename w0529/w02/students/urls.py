from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('writeOK/', views.writeOK, name='writeOK'),
    path('view/<int:no>/', views.view, name='view'),
]