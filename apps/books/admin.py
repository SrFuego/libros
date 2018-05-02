# apps/books/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Book


# Register your models here.
admin.site.register(Book)
