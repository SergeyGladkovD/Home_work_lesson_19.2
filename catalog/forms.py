from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ProductForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "photo",
            "category",
            "price",
            "created_at",
            "owner",
        )

    def clean_name(self):
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        name = self.cleaned_data["name"]
        for word in forbidden_words:
            if word in name:
                raise ValidationError("Вы используете запрещенные слова.")
        return name

    def clean_description(self):
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        description = self.cleaned_data["description"]
        for word in forbidden_words:
            if word in description:
                raise ValidationError("Вы используете запрещенные слова.")
        return description


class ProductModeratorForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("is_publication", "description", "category")


class VersionForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"
