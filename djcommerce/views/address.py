from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from models import Address

class AddressCreateView(CreateView):
    model = Address
    fields = [
        'address_line_1',
        'address_line_2',
        'city',
        'state',
        'zip'
    ]

class AddressDetailView(DetailView):
    model = Address


class AddressListView(ListView):
    model = Address

class AddressUpdateView(UpdateView):
    model = Address
    fields = [
        'address_line_1',
        'address_line_2',
        'city',
        'state',
        'zip'
    ]

class AddressDeleteView(DeleteView):
    model = Address
