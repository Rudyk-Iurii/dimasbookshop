from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    price = models.IntegerField()
    condition = models.CharField(max_length=120, default="Как новая, без следов использования")
    series = models.CharField(max_length=120, blank=True)
    add_info = models.TextField(blank=True)
    reserved = models.BooleanField(default=False)
    promotion = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"id": self.id})
