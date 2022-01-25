from ajax_select.admin import AjaxSelectAdmin
from django.contrib import admin

# Register your models here.
from .models import Product, DeliveryPoint, ProductType

admin.site.register(Product)
admin.site.register(DeliveryPoint)
admin.site.register(ProductType)
