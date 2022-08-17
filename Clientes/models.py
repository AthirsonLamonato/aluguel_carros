from django.db import models


class Cliente(models.Model):
	nome = models.CharField(max_length=50, verbose_name="Nome / Razão Social", help_text="Informe o nome ou razão social")
	cpf = models.IntegerField(verbose_name="CPF / CNPJ", help_text="Informe o CPF ou CNPJ")
	endereco = models.CharField(max_length=50, verbose_name="Endereço", help_text="Informe o endereço")
	telefone = models.IntegerField(verbose_name="Telefone", help_text="Informe o Telefone")

	def __str__(self):
		return self.nome