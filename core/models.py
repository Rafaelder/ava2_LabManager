from django.db import models
from django.contrib.auth.models import User

class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('manutencao', 'Em Manutenção'),
        ('inativo', 'Inativo'),
    ]
    
    nome = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
    ultima_calibragem = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome} ({self.get_status_display()})"

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.laboratorio} - {self.data_inicio}"