from django.urls import path

from . import views

urlpatterns = [
    path(r'perform/', views.perform, name='perform'),
]