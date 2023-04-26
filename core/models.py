from django.db import models
from django.utils.translation import gettext_lazy as _

class TipoVeiculo(models.TextChoices):
    MOTO = "MOTO", _("Moto")
    PEQUENO = "PEQUENO", _("Pequeno")
    MEDIO = "MEDIO", _("Médio")
    GRANDE = "GRANDE", _("Grande")


class Clientes(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=200)
    veiculo = models.CharField(max_length=15)
    placa = models.CharField(max_length=7)

def __str__(self):
        return self.nome


class Servicos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=3)
    

class OrdemServico(models.Model):
    numero = models.IntegerField()
    cliente = models.ForeignKey(Clientes, related_name="cliente", on_delete=models.CASCADE)
    veiculo = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15, choices=TipoVeiculo.choices)
    servico = models.ManyToManyField(Servicos)
    data_hora = models.DateTimeField(auto_now_add=True)
    valor_os = models.DecimalField(max_digits=6, decimal_places=3)
    
