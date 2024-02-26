
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=266, null=True, blank=True)
	category = models.CharField(max_length=266, null=True, blank=True)
	mode = models.CharField(max_length=200, null=True, blank=True, default= "Yard")
	sub_category = models.CharField(max_length=266, null=True, blank=True)
	initial_price = models.FloatField(null=True, blank=True)
	final_price = models.FloatField(null=True, blank=True)
	description = models.TextField(blank=True)
	original_pics = models.ImageField(null=True, blank=True, upload_to="images/")
	pics1 = models.ImageField(null=True, blank=True, upload_to="images/")
	pics2 = models.ImageField(null=True, blank=True, upload_to="images/")
	pics3 =  models.ImageField(null=True, blank=True, upload_to="images/")


	def __str__(self):
		return self.name 
	# +' '+ self.category+' '+ self.sub_category

	def get_absolute_url(self):
		return reverse('add_product')

class Cart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quantity = models.FloatField(null=True, blank=True, default=1.0)
	
	def __str__(self):
		return self.user.username + ' carts '+ self.product.name
	


class Order(models.Model):
	total_price = models.FloatField()
	order_id = models.CharField(max_length=250, default="ABC")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	quantity = models.FloatField(null=True, blank=True)
	username = models.CharField(max_length=250, null=True, blank=True)
	email = models.CharField(max_length=250, null=True, blank=True)
	item = models.CharField(max_length=250, null=True, blank=True)
	rate = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.order_id




# 	# def serialize(self):
#  #       return {
#  #            "id": self.id,
#  #            "quantity":self.quantity
#  #       }
	
class Slide(models.Model):
	slide1pics = models.ImageField(null=True, blank=True)
	slide1heading = models.CharField(max_length=250, null=True, blank=True)
	slide1subheading = models.CharField(max_length=250, null=True, blank=True)
	slide1writeup = models.CharField(max_length=250, null=True, blank=True)

	slide2pics = models.ImageField(null=True, blank=True)
	slide2heading = models.CharField(max_length=250, null=True, blank=True)
	slide2subheading = models.CharField(max_length=250, null=True, blank=True)
	slide2writeup = models.CharField(max_length=250, null=True, blank=True)

	slide3pics = models.ImageField(null=True, blank=True)
	slide3heading = models.CharField(max_length=250, null=True, blank=True)
	slide3subheading = models.CharField(max_length=250, null=True, blank=True)
	slide3writeup = models.CharField(max_length=250, null=True, blank=True)

	slide4pics = models.ImageField(null=True, blank=True)
	slide4heading = models.CharField(max_length=250, null=True, blank=True)
	slide4subheading = models.CharField(max_length=250, null=True, blank=True)
	slide4writeup = models.CharField(max_length=250, null=True, blank=True)

	slide5pics = models.ImageField(null=True, blank=True)
	slide5heading = models.CharField(max_length=250, null=True, blank=True)
	slide5subheading = models.CharField(max_length=250, null=True, blank=True)
	slide5writeup = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return str(self.slide1heading) 
	
	def get_absolute_url(self):
		return reverse('add_slide')


