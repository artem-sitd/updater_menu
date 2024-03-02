from django.db import models
from django.utils.text import slugify


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
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
