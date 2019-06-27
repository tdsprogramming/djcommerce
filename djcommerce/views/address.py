from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from djcommerce.models import Address

class AddressCreateView(CreateView):
    model = Address
    fields = [
        'address_line_1',
        'address_line_2',
        'city',
        'state',
        'zip'
    ]
    template_name = 'address/create.html'

class AddressDetailView(DetailView):
    model = Address
    template_name = 'address/detail.html'

class AddressListView(ListView):
    model = Address
    template_name = 'address/list.html'

class AddressUpdateView(UpdateView):
    model = Address
    fields = [
        'address_line_1',
        'address_line_2',
        'city',
        'state',
        'zip'
    ]
    template_name = 'address/update.html'

class AddressDeleteView(DeleteView):
    model = Address
    template_name = 'address.delete.html'
