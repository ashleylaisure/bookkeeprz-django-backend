from django.contrib import admin
from .models import Book, Journal, Bookshelf

# Register your models here.

admin.site.register(Book)
admin.site.register(Journal)
admin.site.register(Bookshelf)
