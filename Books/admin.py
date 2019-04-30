from django.contrib import admin
from .models import Book

# Register your models here.
class BookModelAdmin(admin.ModelAdmin):
	list_display = ["title", "price", "promotion"]


	search_fields = ["title", "author"]
	class Meta:
		model = Book


admin.site.register(Book, BookModelAdmin)