from django.urls import path
from catalog.views import ProductListView, ProductDetailView, contacts, ProductCreateView, VersionListView, \
    VersionDetailView, VersionCreateView, VersionUpdateView, VersionDeleteView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', contacts, name='contacts'),
    path('versions/', VersionListView.as_view(), name='version_list'),
    path('version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('version/create/', VersionCreateView.as_view(), name='version_create'),
    path('version/<int:pk>/edit/', VersionUpdateView.as_view(), name='version_update'),
    path('version/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),
]
