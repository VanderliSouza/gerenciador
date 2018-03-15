from django.db import models


class ItemAgenda(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.TextField(max_length=100)
	descricao = models.TextField()