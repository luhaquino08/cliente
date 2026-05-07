from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome completo", max_length=100)
    cpf = models.CharField(verbose_name="CPF", max_length=14)
    telefone = models.CharField(verbose_name="Telefone", max_length=14)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")

    def __str__(self):
        return self.nome