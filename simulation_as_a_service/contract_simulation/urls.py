from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='contract-simulation-home'),
    path('ran_simulation/', views.ranSimulation, name='ran-simulation'),
]
