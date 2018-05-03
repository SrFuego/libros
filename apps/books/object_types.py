# apps/books/object_types.py
# Python imports


# Django imports


# Third party apps imports
from graphene_django.types import DjangoObjectType


# Local imports
from .models import Collection, Course, Editorial, Kind, Pdf


# Create your schemas here.
class CollectionType(DjangoObjectType):
    class Meta:
        model = Collection


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class EditorialType(DjangoObjectType):
    class Meta:
        model = Editorial


class KindType(DjangoObjectType):
    class Meta:
        model = Kind


class PdfType(DjangoObjectType):
    class Meta:
        model = Pdf
