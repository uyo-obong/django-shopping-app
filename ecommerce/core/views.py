from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic as g
import pdb


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)


class ListViewCategory(g.ListView):
    model = Product
    template_name = 'categories/category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category = self.category)

    def get_context_data(self, **kwargs):
        context = super(ListViewCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context










