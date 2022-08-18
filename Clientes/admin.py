from django.contrib import admin

from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    search_fields= ('nome',)

admin.site.register(Cliente, ClienteAdmin)
