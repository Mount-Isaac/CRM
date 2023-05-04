from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	message = models.TextField(blank=True, default="Leave message here")


	def __str__(self):
		return f'{self.name}"s message'