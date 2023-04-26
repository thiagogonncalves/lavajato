from django.db import models


class cliente(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=11)
    veiculo = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)
    observacao = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.nome