from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from .models import Category

class CategoryCreateView(CreateView):
    model = Category
    fields = [
        'name'
    ]

class CategoryDetailView(DetailView):
    model = Category

class CategoryListView(ListView):
    model = Category

class CategoryUpdateView(UpdateView):
    model = Category
    fields = [
        'name'
    ]

class CategoryDeleteView(DeleteView):
    model = Category
