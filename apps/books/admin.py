# apps/books/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Course, Editorial, Kind, Pdf, Topic


# Register your models here.
admin.site.register(Course)
admin.site.register(Editorial)
admin.site.register(Kind)
admin.site.register(Pdf)
admin.site.register(Topic)
