from django.forms import ModelForm, inlineformset_factory

from .models import Product, DeliveryPoint


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class DeliveryPointForm(ModelForm):
    class Meta:
        model = DeliveryPoint
        fields = '__all__'


DeliveryPointInlineFormset = inlineformset_factory(
    Product,
    DeliveryPoint,
    fields=['address', ],
    extra=1
)