# apps/books/object_types.py
# Python imports


# Django imports


# Third party apps imports
from graphene_django.types import DjangoObjectType


# Local imports
from .models import Course, Editorial, Kind, Pdf, Topic


# Create your schemas here.
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


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
