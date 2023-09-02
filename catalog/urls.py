from django.urls import path

from catalog.views import home, contacts, product_details

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:product_id>/', product_details, name='product_detail'),
]
