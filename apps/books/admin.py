# apps/books/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from dynamic_raw_id.admin import DynamicRawIDMixin


# Local imports
from .models import Course, Editorial, Kind, Pdf, Topic


# Register your models here.
@admin.register(Pdf)
class PdfModelAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    dynamic_raw_id_fields = ("topic",)
    filter_horizontal = ("topic",)


admin.site.register(Course)
admin.site.register(Editorial)
admin.site.register(Kind)
admin.site.register(Topic)
