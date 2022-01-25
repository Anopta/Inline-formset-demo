from django.urls import path

from .views import ProductCreateView, ProductUpdateView, ProductsListView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name="product_list"),
    path('products/create/', ProductCreateView.as_view(), name="create_product"),
    path('products/<int:pk>/', ProductUpdateView.as_view(), name="update_product")
]