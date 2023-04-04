from django.contrib import admin
from .models import Product, Detail, Customer

admin.site.register(Product)
admin.site.register(Detail)
admin.site.register(Customer)

# Register your models here.