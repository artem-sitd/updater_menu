from django import template
from menu.models import Category

register = template.Library()


@register.inclusion_tag('templates/base.html')
def draw_menu(menu_name):
    categories = Category.objects.filter(parent__isnull=True).prefetch_related('subcategory')

    def add_subcategories(category, level=0):
        category.has_children = bool(category.subcategory.all())
        category.level = level
        if category.has_children:
            for subcategory in category.subcategory.all():
                add_subcategories(subcategory, level + 1)

    for category in categories:
        add_subcategories(category)

    return {'categories': categories, 'menu_name': menu_name}
