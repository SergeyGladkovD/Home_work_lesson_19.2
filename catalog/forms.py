from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'photo', 'category', 'price', 'created_at')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        name = self.cleaned_data['name']
        if name in forbidden_words:
            raise ValidationError('Вы используете запрещенные слова.')
        return name

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        description = self.cleaned_data['description']
        for word in forbidden_words:
            if word in description:
                raise ValidationError('Вы используете запрещенные слова.')
        return description


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
