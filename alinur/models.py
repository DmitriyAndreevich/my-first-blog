from django.db import models

class Contact (models.Model):
	your_name = models.CharField(max_length=255)
	your_email = models.EmailField(max_length=75)
	your_phone = models.CharField(max_length=255)
	your_message = models.TextField()

