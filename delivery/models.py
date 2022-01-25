import datetime

from django.db import models


# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product Type name', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    verbose_name = "Product Type"
    verbose_name_plural = "Product Types"


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="Product Name", null=True, blank=True)
    product_type = models.ForeignKey(ProductType, verbose_name='Product Type', on_delete=models.SET_NULL, null=True,
                                     blank=True)
    delivery_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name="Delivery Date")
    attachment = models.FileField(
        verbose_name="Attachment", upload_to="media", blank=True
    )

    def __str__(self):
        return f"{self.product_name}"

    verbose_name = "Product"
    verbose_name_plural = "Products"


class DeliveryPoint(models.Model):
    address = models.CharField(max_length=255, verbose_name="Address", null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.SET_NULL, null=True,
                                blank=True)

    def __str__(self):
        return f"{self.address}"

    verbose_name = "Delivery Point"
    verbose_name_plural = "Delivery Points"
