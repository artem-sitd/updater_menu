from django.views.generic import DetailView
from .models import Category


class CategoryDetail(DetailView):
    slug_field = "slug"
    model = Category
    template_name = "menu/category_detail.html"
    context_object_name = "category"
