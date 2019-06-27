from django.views.generic import  DetailView, UpdateView, DeleteView
from djcommerce.models import Cart

class CartDetailView(DetailView):
    model = Cart
    template_name= 'cart/detail.html'

class CartUpdateView(UpdateView):
    model = Cart
    fields = [
        'products'
    ]
    template_name= 'cart/update.html'

class CartDeleteView(DeleteView):
    model = Cart
    template_name= 'cart/delete.html'
