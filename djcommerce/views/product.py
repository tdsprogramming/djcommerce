from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from models import Product

class ProductCreateView(CreateView):
    model = Product
    fields = [
        'name',
        'categories',
        'stock',
        'price',
        'configurations'
    ]

class ProductDetailView(DetailView):
    model = Product

class OrderListView(ListView):
    model = Product

class OrderUpdateView(UpdateView):
    model = Product
    fields = [
        'name',
        'categories',
        'stock',
        'price',
        'configurations'
    ]

class OrderDeleteView(DeleteView):
    model = Product
