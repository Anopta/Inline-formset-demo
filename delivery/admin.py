from django.contrib import admin

# Register your models here.
from .models import *

class DeliveryInline(admin.StackedInline):
    '''Stacked Inline View for '''
    model = DeliveryPoint
    min_num = 0
    max_num = 3
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ DeliveryInline]

admin.site.register(ProductType)