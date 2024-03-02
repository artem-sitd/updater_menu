from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "slug")
    prepopulated_fields = {"slug": ("title",)}  # new


admin.site.register(Category, CategoryAdmin)
