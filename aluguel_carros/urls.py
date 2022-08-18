from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from Carros.views import CarListView

admin.site.site_header = 'Locação de Veículos'

urlpatterns = [
    path('', admin.site.urls),
]
