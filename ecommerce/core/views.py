from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from ecommerce.core.mixins import ExtraContextMixin
from .models import Product, Category
from django.views import generic as g


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)


class ListViewCategory(g.ListView):
    model = Product
    paginate_by = 6
    template_name = 'categories/category.html'

    def get_queryset(self):
        self.categories = Category.objects.all()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category = self.category)

    def get_context_data(self, **kwargs):
        context = super(ListViewCategory, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        context['category'] = self.category
        return context










