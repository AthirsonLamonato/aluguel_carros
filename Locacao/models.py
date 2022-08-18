from click import option
from django.db import models
from django.forms import ValidationError
from requests import options
from Clientes.models import Cliente
from Carros.models import Carro
from datetime import datetime


def valida_carro_data_unico(carro):        
	carros_alugados = Locacao.objects.filter( carro = carro, data_entrega = None, data_retirada__lt=datetime.now())		
	if carros_alugados:
		raise ValidationError('Este carro já está em uso')

class Locacao(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", help_text="Selecione o Cliente")
	carro = models.ForeignKey(Carro, on_delete=models.CASCADE, verbose_name="Carro", help_text="Selecione o Carro", validators=[valida_carro_data_unico])
	data_retirada = models.DateField(verbose_name="Data de Retirada", help_text="Informe a Data de Retirada do Veículo")
	data_entrega_prevista = models.DateField(verbose_name="Previsão de entrega", help_text="Informe a data que o veículo deve ser devolvido")
	data_entrega = models.DateField(verbose_name="Data de entrega", null=True, blank=True, help_text="Informe a data que o veículo foi devolvido")
	intencao_uso = models.CharField(max_length=100, verbose_name="Intenção de uso", help_text="Informe a intenção de utilização do veículo")
	cnh = models.IntegerField(verbose_name="CNH", help_text="Informe a CNH")
	status_options = (
		('P', 'Pago'),
		('A', 'Aberto'),
		('C', 'Cancelado'),
	)
	status = models.CharField(max_length=1, choices=status_options, default='A')

	class Meta:
		verbose_name = "Locação"
		verbose_name_plural = "Locações"

	def save(self, *args,**kwargs):    
		carro = Carro.objects.get(id=self.carro.id)
		if self.data_entrega:			
			carro.status = 'L'
			carro.save(update_fields=['status'])
		else:
			carro.status = 'O'
			carro.save(update_fields=['status'])
		super(Locacao, self).save(*args, **kwargs)
		return

	def __str__(self):
		identificacao = ' '.join([str(self.id), '-','[', str(self.carro.placa), ']', str(self.cliente)])
		return identificacao

	

