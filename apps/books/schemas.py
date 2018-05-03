# apps/books/schemas.py
# Python imports


# Django imports


# Third party apps imports
import graphene
from graphene_django.types import DjangoObjectType


# Local imports
from .models import Pdf


# Create your schemas here.
class PdfType(DjangoObjectType):
    class Meta:
        model = Pdf


class PdfQuery(object):
    all_pdfs = graphene.List(
        PdfType, collection=graphene.Int(), course=graphene.Int(),
        kind=graphene.Int())
    pdf = graphene.Field(PdfType, id=graphene.Int(), name=graphene.String())

    def resolve_all_pdfs(self, info, **kwargs):
        return Pdf.objects.filter(**kwargs)

    def resolve_pdf(self, info, **kwargs):
        return Pdf.objects.get(**kwargs)
