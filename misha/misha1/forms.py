from django import forms

from .models import Product, Detail


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'


class CustomerForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    date = forms.DateField(widget=forms.SelectDateWidget)