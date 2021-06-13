from django.contrib import admin

from .models import City, Customer, Product, Provider


admin.site.register(City)
admin.site.register(Customer)
admin.site.register(Provider)
admin.site.register(Product)
