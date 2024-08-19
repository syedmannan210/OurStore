from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Orders
from .models import Product,Contact
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)