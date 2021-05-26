from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

# Create your models here.

# User Model
class User (AbstractUser):
	is_seller  = models.BooleanField(default=False)
	is_buyer = models.BooleanField(default=False)

# Optional Tags to be attached with each product
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

# Products added by various sellers
class Products(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='seller')
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

# Products ordered by variou buyers
class Orders(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='buyer')
	product = models.ForeignKey(Products, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.Order.name

