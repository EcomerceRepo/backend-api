from .models import Product
from django.http import Http404

def get_product(pk):
    try:
        return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")