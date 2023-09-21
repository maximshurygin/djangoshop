from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


class VersionListView(ListView):
    model = Version
    template_name = 'catalog/version_list.html'
    context_object_name = 'versions'


class VersionDetailView(DetailView):
    model = Version
    template_name = 'catalog/version_detail.html'
    context_object_name = 'version'


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('version_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('version_list')

    def form_valid(self, form):
        if form.cleaned_data['is_current_version']:
            Version.objects.filter(product=form.instance.product).exclude(pk=form.instance.pk).update(
                is_current_version=False)
        return super().form_valid(form)


class VersionDeleteView(DeleteView):
    model = Version
    template_name = 'catalog/version_confirm_delete.html'
    success_url = reverse_lazy('version_list')
