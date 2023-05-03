from django.db import models

# Create your models here.

class crm_model(models.Model):
	def __init__(self):
		self.model_name = "testing github push"
	def __str__(self):
		return f'{self.model_name.capitalize()}'