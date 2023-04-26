from django.db import models

class servicos(models.Model):
    nome_servico = models.CharField(max_length=150)
    descricao = models.TextField(max_length=300, null=True, blank=False)
    valor = models.CharField(max_length=3)


    def __str__(self):
        return self().nome_servico()
