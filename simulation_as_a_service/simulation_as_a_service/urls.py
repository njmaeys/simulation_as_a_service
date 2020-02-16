from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='site-home'),
    path('contract_simulation/', include('contract_simulation.urls')),
    path('admin/', admin.site.urls),
]
