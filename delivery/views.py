# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from .forms import ProductForm, DeliveryPointInlineFormset
from .models import Product


class ProductsListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'delivery/product_create_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['delivery_point_formset'] = DeliveryPointInlineFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_point_formset = DeliveryPointInlineFormset(request.POST, request.FILES)
        if form.is_valid() and delivery_point_formset.is_valid():
            return self.form_valid(form, delivery_point_formset)
        else:
            return self.form_invalid(form, delivery_point_formset)

    def form_valid(self, form, delivery_point_formset):
        self.object = form.save(commit=False)
        self.object.save()
        delivery_points = delivery_point_formset.save(commit=False)
        for delivery_point in delivery_points:
            delivery_point.product = self.object
            delivery_point.save()
        return redirect(reverse("product_list"))

    def form_invalid(self, form, delivery_point_formset):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_point_formset=delivery_point_formset
                                  )
        )


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'delivery/product_create_form.html'
    success_url = '/products'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['delivery_point_formset'] = DeliveryPointInlineFormset(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        delivery_points = DeliveryPointInlineFormset(request.POST, request.FILES, instance=self.object)

        if delivery_points.is_valid() and form.is_valid():
            delivery_points.save()
            form.save()
            return redirect('/products/')
        else:
            return redirect("update_product", pk=self.object.id)
