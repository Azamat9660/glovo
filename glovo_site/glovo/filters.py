from .models import Store,  Product
from django_filters import FilterSet

class StoreFilter(FilterSet):
    class Meta:
        model = Store
        fields = {
            'store_name': ['exact'],


        }

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'product_name': ['exact'],
            'price' : ['gt', 'lt']
        }