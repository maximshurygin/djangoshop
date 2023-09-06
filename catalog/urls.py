from django.urls import path
from catalog.views import ProductListView, ProductDetailView, contacts

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', contacts, name='contacts'),
]
