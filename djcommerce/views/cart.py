from django.views.generic import  DetailView, UpdateView, DeleteView
from models import Cart

class CartDetailView(DetailView):
    model = Cart

class CartUpdateView(UpdateView):
    model = Cart
    fields = [
        'products'
    ]

class CartDeleteView(DeleteView):
    model = Cart
