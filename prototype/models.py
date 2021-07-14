from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class Meeting_location(models.Model):
	location=models.CharField(max_length=50, default='')

	latitude=models.FloatField(default=0.0)
	longitude=models.FloatField(default=0.0)

	class Meta:
		ordering=['-location']

	def __str__(self):
		return self.name

class Req_gui(models.Model):
	name=models.CharField(max_length=15)
	location=models.CharField(max_length=50, default='')

	latitude=models.FloatField(default=0.0)
	longitude=models.FloatField(default=0.0)

	introduce=models.CharField(max_length=50)
	email=models.CharField(max_length=30, null=True)

	class Meta:
		ordering=['-name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('Req_gui-detail', args=[str(self.id)])

class Req_use(models.Model):
	name=models.CharField(max_length=15)
	location=models.CharField(max_length=50, default='')

	latitude=models.FloatField(default=0.0)
	longitude=models.FloatField(default=0.0)

	introduce=models.CharField(max_length=50)
	email=models.CharField(max_length=30, null=True)

	class Meta:
		ordering=['-name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('Req_use-detail', args=[str(self.id)])

class User_info(models.Model):
	name=models.CharField(max_length=15)
	password=models.CharField(max_length=20)
	dis_identify_num=models.CharField(max_length=14, null=True)
	email=models.CharField(max_length=30, null=True)

	class Meta:
		ordering=['-name']

	def __str__(self):
		return self.name

class Guide_info(models.Model):
	name=models.CharField(max_length=15)
	password=models.CharField(max_length=20)
	identify_num=models.CharField(max_length=14, null=True)
	email=models.CharField(max_length=30, null=True)

	class Meta:
		ordering=['-name']

	def __str__(self):
		return self.name