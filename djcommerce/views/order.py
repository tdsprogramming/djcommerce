from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from .models import Order

class OrderCreateView(CreateView):
    model = Order
    fields = [
        'products'
    ]

class OrderDetailView(DetailView):
    model = Order

class OrderListView(ListView):
    model = Order

class OrderUpdateView(UpdateView):
    model = Order
    fields = [
        'products'
    ]

class OrderDeleteView(DeleteView):
    model = Order
