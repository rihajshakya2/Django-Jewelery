from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Ring)
admin.site.register(Necklace)
admin.site.register(Earring)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
