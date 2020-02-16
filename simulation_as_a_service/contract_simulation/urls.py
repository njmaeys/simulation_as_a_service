from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='contract-simulation-home'),
]
