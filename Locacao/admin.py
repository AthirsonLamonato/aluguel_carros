from django.contrib import admin

from .models import Locacao
from Carros.models import Carro

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carro', 'data_retirada','data_entrega_prevista', 'data_entrega' ,'status')
    search_fields= ('cliente__nome',)
    list_filter = ('carro', 'data_retirada','data_entrega_prevista', 'data_entrega' ,'status')

    
    '''
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.my_id_for_formfield = obj.id
        return super(LocacaoAdmin, self).get_form(request, obj, **kwargs)
        '''
    
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        try:
            my_id_for_formfield = request.resolver_match.kwargs['object_id']
        except:
            my_id_for_formfield = None
        if db_field.name == "carro" and  my_id_for_formfield == None :
            kwargs["queryset"] = Carro.objects.filter(status='L')
        return super(LocacaoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        
    

admin.site.register(Locacao, LocacaoAdmin)
