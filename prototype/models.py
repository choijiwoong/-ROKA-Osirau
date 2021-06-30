from django.db import models

# Create your models here.

class Servicer(models.Model):
	name=models.CharField(max_length=15)
	location=models.CharField(max_length=50, default='')

	latitude=models.FloatField(default=0.0)
	longitude=models.FloatField(default=0.0)

	class Meta:
		ordering=['-name']

	def __str__(self):
		return self.name

class User(models.Model):
	name=models.CharField(max_length=15)
	location=models.CharField(max_length=50, default='')

	latitude=models.FloatField(default=0.0)
	longitude=models.FloatField(default=0.0)

	class Meta:
		ordering=['-name']

	def __str__(self):
		return self.name

class Meeting_location(models.Model):
	location=models.CharField(max_length=50, default='')

	latitude=models.FloatField(default=0.0)
	longitude=models.FloatField(default=0.0)

	class Meta:
		ordering=['-location']

	def __str__(self):
		return self.name

