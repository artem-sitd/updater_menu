from django.db import models
from django.utils.text import slugify

import re
from unidecode import unidecode

def custom_slugify(value):
    """
    Convert to lowercase, remove non-word characters,
    and convert spaces to hyphens.
    """
    value = unidecode(value)  # convert unicode to ascii
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()  # удаляем все символы кроме букв, цифр, пробелов и дефисов
    value = re.sub(r'[-\s]+', '-', value)  # заменяем пробелы и повторяющиеся дефисы на одиночный дефис
    return value


class Category(models.Model):
    title = models.CharField(max_length=40)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Родитель",
        related_name="subcategory",
    )
    slug = models.SlugField(unique=True, null=True)  # new

    def __str__(self: "object of class Category") -> str:
        return f"{self.title} ID = {self.id}"

    def save(self, *args, **kwargs):
        self.slug = custom_slugify(self.title)
        super(Category, self).save(*args, **kwargs)
