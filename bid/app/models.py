from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
  is_customer = models.BooleanField(default=False)

class Customer(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100,null=True,blank=True)
  email =models.EmailField(max_length=100)
  location = models.CharField(max_length=100,null=True,blank=True)
  def __str__(self):
    return str(self.id)

class Product(models.Model):
  user=models.ForeignKey(Customer,on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()
  photo = models.ImageField(upload_to='images')
  min_bid_price= models.CharField(max_length=50)
  auctionEndTime=models.TimeField()

  def __str__(self):
    return str(self.id)

  def get_absolute_url(self):
    return reverse('product-detail', args=[str(self.id)])

class Bid(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  user = models.ForeignKey(Customer,on_delete=models.CASCADE)
  bid_amount = models.CharField(max_length=20)

  def __str__(self):
    return str(self.id)

