from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from djcommerce.models import Product

class ProductCreateView(CreateView):
    model = Product
    fields = [
        'name',
        'categories',
        'stock',
        'price',
        'configurations'
    ]
    template_name= 'product/create.html'

class ProductDetailView(DetailView):
    model = Product
    template_name= 'product/detail.html'

class OrderListView(ListView):
    model = Product
    template_name= 'product/list.html'

class OrderUpdateView(UpdateView):
    model = Product
    fields = [
        'name',
        'categories',
        'stock',
        'price',
        'configurations'
    ]
    template_name= 'product/update.html'

class OrderDeleteView(DeleteView):
    model = Product
    template_name= 'product/delete.html'
