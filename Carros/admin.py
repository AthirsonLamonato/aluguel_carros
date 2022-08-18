from django.contrib import admin

from .models import Marca, Modelo, Carro

class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'valor_locacao','status')
    search_fields= ('placa','modelo__modelo',)
    list_filter = ('status','modelo')

    

admin.site.register(Carro, CarroAdmin)

admin.site.register([Marca, Modelo])
