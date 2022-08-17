from django.db import models

class Marca(models.Model):
	marca = models.CharField(max_length=30)

	def __str__(self):
		return self.marca

class Modelo(models.Model):
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default="Modelo Desconhecido")
	modelo = models.CharField(max_length=30)

	def __str__(self):
		identificacao = ' '.join([str(self.marca), str(self.modelo)])
		return identificacao

class Carro(models.Model):
	modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, default="Modelo Desconhecido", verbose_name="Marca/Modelo do Veículo", help_text="Selecione o modelo do veículo")
	placa = models.CharField(max_length=10, verbose_name="Placa do Veículo",help_text="Informe a placa")
	cor = models.CharField(max_length=50, verbose_name="Cor do Veículo",help_text="Informe a cor")
	ano = models.IntegerField(verbose_name="Ano do Veículo", help_text="Informe o ano")
	qtd_portas = models.CharField(max_length=50, verbose_name="Quantidade de Portas", help_text="Informe a quantidade de portas")


	combustivel_tipo = (
			('DI', 'Diesel'),
			('ET', 'Etanol'),
			('GA', 'Gasolina'),
			('BI', 'Biodisel'),
			('EN', 'Elétrico'),
			('GN', 'Gás Natural Veicular'),
	)

	combustivel = models.CharField(choices=combustivel_tipo, max_length=2, verbose_name="Tipo de combustível", help_text="Informe o tipo de combustível")
	chassi = models.CharField(max_length=50, verbose_name="Número do Chassi", help_text="Informe o número do chassi")
	renavam = models.IntegerField(verbose_name="Renavam", help_text="Informe o renavam")
	nr_hodometro = models.IntegerField(verbose_name="Número hodômetro", help_text="Informe o Número marcado pelo hodômetro")
	valor_locacao = models.DecimalField(verbose_name="Valor de Locação", max_digits=19, decimal_places=2, help_text="Informe o valor")

	def __str__(self):
		identificacao = ' '.join(['[', str(self.placa), ']', str(self.modelo.marca), str(self.modelo.modelo)])
		return identificacao
