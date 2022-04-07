from django.contrib import admin
from .models import *
# Register your model(s here.
admin.site.register(User)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display=['id','name','email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display=['id','name','min_bid_price','auctionEndTime']