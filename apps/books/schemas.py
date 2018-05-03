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
    all_pdfs = graphene.List(PdfType)
    pdf = graphene.Field(PdfType, id=graphene.Int(), name=graphene.String())

    def resolve_all_pdfs(self, info, **kwargs):
        return Pdf.objects.all()

    def resolve_pdf(self, info, **kwargs):
        pdf_id = kwargs.get("id")
        pdf_name = kwargs.get("name")
        if pdf_id is not None:
            return Pdf.objects.get(pk=pdf_id)
        if pdf_name is not None:
            return Pdf.objects.get(name=pdf_name)
