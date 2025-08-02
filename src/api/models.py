# src/api/models.py
from django.db import models
from django.utils import timezone

class Profissional(models.Model):
    nome_social = models.CharField(max_length=100)
    profissional = models.CharField(max_length=100)  # corrigido: precisa do max_length
    endereco = models.CharField(max_length=255)      # corrigido: precisa do max_length
    contato = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_social
    

class Consulta(models.Model):
    data = models.DateField()
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        related_name='consultas',
        verbose_name="Profissional"
    )


def __str__(self):
        return f"{self.profissional.nome_social} - {self.data.strftime('%d/%m/%Y')}"
