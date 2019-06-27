from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from djcommerce.models import Category

class CategoryCreateView(CreateView):
    model = Category
    fields = [
        'name'
    ]
    template_name= 'category/create.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name= 'category/detail.html'

class CategoryListView(ListView):
    model = Category
    template_name= 'category/list.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = [
        'name'
    ]
    template_name= 'category/update.html'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name= 'category/delete.html'
