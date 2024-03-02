from django.db import models

import re
from unidecode import unidecode


def custom_slugify(value):
    value = unidecode(value)
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
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
