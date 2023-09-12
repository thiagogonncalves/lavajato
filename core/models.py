from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    veiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.nome


class Servico(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=200)
    
    