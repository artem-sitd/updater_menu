from django.db import models
from menu.models import Category


class Service(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500, default='описание услуги', blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return f'ID: {self.pk}, {self.title}. > Категория: {self.category} <'