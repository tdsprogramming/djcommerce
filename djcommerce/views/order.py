from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from djcommerce.models import Order

class OrderCreateView(CreateView):
    model = Order
    fields = [
        'products'
    ]
    template_name= 'order/create.html'

class OrderDetailView(DetailView):
    model = Order
    template_name= 'order/detail.html'

class OrderListView(ListView):
    model = Order
    template_name= 'order/list.html'

class OrderUpdateView(UpdateView):
    model = Order
    fields = [
        'products'
    ]
    template_name= 'order/update.html'

class OrderDeleteView(DeleteView):
    model = Order
    template_name= 'order/delete.html'
