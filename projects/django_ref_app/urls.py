from django.urls import path
from .views import (
    index,
    add_customer,
    add_product,
    update_product,
    delete_product,
    patch_product
)
urlpatterns = [
    path("", index, name='index'),
    path("customer/", add_customer, name='add_customer'),
    path("product/", add_product, name='add_product'),
    path("product/<int:pk>/", update_product, name='update_product'),
    path("pdt/<int:pk>/", delete_product, name='delete_product'),
    path("pdt/exist/<int:pk>/", patch_product, name='patch_product'),
]
