from django.db import models


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

    def __str__(self: 'object of class Category') -> str:
        return f"{self.title} ID = {self.id}"
