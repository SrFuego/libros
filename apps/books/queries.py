# apps/books/queries.py
# Python imports


# Django imports


# Third party apps imports
import graphene


# Local imports
from .models import Collection, Course, Editorial, Kind, Pdf
from .object_types import (
    CollectionType, CourseType, EditorialType, KindType, PdfType,)


# Create your schemas here.
class CollectionQuery(object):
    all_collections = graphene.List(CollectionType)

    def resolve_all_collections(self, info, **kwargs):
        return Collection.objects.filter(**kwargs)


class CourseQuery(object):
    all_courses = graphene.List(CourseType)

    def resolve_all_courses(self, info, **kwargs):
        return Course.objects.filter(**kwargs)


class EditorialQuery(object):
    all_editorials = graphene.List(EditorialType)

    def resolve_all_editorials(self, info, **kwargs):
        return Editorial.objects.filter(**kwargs)


class KindQuery(object):
    all_kinds = graphene.List(KindType)

    def resolve_all_kinds(self, info, **kwargs):
        return Kind.objects.filter(**kwargs)


class PdfQuery(object):
    all_pdfs = graphene.List(
        PdfType, collection=graphene.Int(), course=graphene.Int(),
        kind=graphene.Int())
    pdf = graphene.Field(PdfType, id=graphene.Int(), name=graphene.String())

    def resolve_all_pdfs(self, info, **kwargs):
        return Pdf.objects.filter(**kwargs)

    def resolve_pdf(self, info, **kwargs):
        return Pdf.objects.get(**kwargs)
