from django import forms
from .models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)

    def clean(self):
        cleaned_data = super().clean()
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in forbidden_words:
            if word in name or word in description:
                raise forms.ValidationError(f"'{word}' недопустимо в названии или описании!")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
