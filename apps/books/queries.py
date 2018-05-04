# apps/books/queries.py
# Python imports


# Django imports


# Third party apps imports
import graphene


# Local imports
from .models import Course, Editorial, Kind, Pdf, Topic
from .object_types import (
    CourseType, EditorialType, KindType, PdfType, TopicType,)


# Create your schemas here.
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
        PdfType, course=graphene.Int(), kind=graphene.Int())
    pdf = graphene.Field(PdfType, id=graphene.Int(), name=graphene.String())

    def resolve_all_pdfs(self, info, **kwargs):
        return Pdf.objects.filter(**kwargs)

    def resolve_pdf(self, info, **kwargs):
        return Pdf.objects.get(**kwargs)


class TopicQuery(object):
    all_topics = graphene.List(TopicType)

    def resolve_all_topics(self, info, **kwargs):
        return Topic.objects.filter(**kwargs)
