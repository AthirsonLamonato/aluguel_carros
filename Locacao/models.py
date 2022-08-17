from django.db import models
from Clientes.models import Cliente
from Carros.models import Carro

class Locacao(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", help_text="Selecione o Cliente")
	carro = models.ForeignKey(Carro, on_delete=models.CASCADE, verbose_name="Carro", help_text="Selecione o Carro")
	data_retirada = models.DateField(verbose_name="Data de Retirada", help_text="Informe a Data de Retirada do Veículo")
	data_entrega_prevista = models.DateField(verbose_name="Previsão de entrega", help_text="Informe a data que o veículo deve ser devolvido")
	data_entrega = models.DateField(verbose_name="Data de entrega", null=True, blank=True, help_text="Informe a data que o veículo foi devolvido")
	intencao_uso = models.CharField(max_length=100, verbose_name="Intenção de uso", help_text="Informe a intenção de utilização do veículo")
	cnh = models.IntegerField(verbose_name="CNH", help_text="Informe a CNH")

	def __str__(self):
		identificacao = ' '.join(['[', str(self.carro.placa), ']', str(self.cliente)])
		return identificacao