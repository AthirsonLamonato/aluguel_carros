from django.contrib import admin

from .models import Marca, Modelo, Carro

admin.site.register([Carro, Marca, Modelo])
