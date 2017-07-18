from __future__ import unicode_literals

from django.db import models

class Car(models.Model):
	brand=models.CharField(max_length=20)
	milage=models.IntegerField()
	year=models.CharField(max_length=5, blank=True, null=True)
	def __str__(self):
		return "{}:{}".format(self.id, self.brand)

class Customer(models.Model):
	name=models.CharField(max_length=100)
	tel=models.CharField(max_length=20)
	def __str__(self):
		return "{}".format(self.name)

class Rent(models.Model):
	#on_delete=models.CASCADE
	car=models.ForeignKey(Car, on_delete=models.CASCADE)
	customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	promotion_code=models.CharField(max_length=20,blank=True, null=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	#hi
