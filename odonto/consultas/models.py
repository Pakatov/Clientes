from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=16)
    telefone = models.CharField(max_length=16)
    endereco = models.CharField(max_length=100)
    foto = models.ImageField(default="user.jpg", upload_to='consultas/static/images/')