from django.views.generic import ListView

from Carros.models import Carro

class CarListView(ListView):
    model = Carro
    template_name = 'car-list.html'
